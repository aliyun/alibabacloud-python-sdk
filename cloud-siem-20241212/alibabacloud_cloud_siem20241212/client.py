# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloud_siem20241212 import models as cloud_siem_20241212_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def check_upgrade_item_with_options(
        self,
        request: cloud_siem_20241212_models.CheckUpgradeItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CheckUpgradeItemResponse:
        """
        @summary 检查升级项
        
        @param request: CheckUpgradeItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUpgradeItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.upgrade_item_id):
            body['UpgradeItemId'] = request.upgrade_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckUpgradeItem',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CheckUpgradeItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_upgrade_item_with_options_async(
        self,
        request: cloud_siem_20241212_models.CheckUpgradeItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CheckUpgradeItemResponse:
        """
        @summary 检查升级项
        
        @param request: CheckUpgradeItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUpgradeItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.upgrade_item_id):
            body['UpgradeItemId'] = request.upgrade_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckUpgradeItem',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CheckUpgradeItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_upgrade_item(
        self,
        request: cloud_siem_20241212_models.CheckUpgradeItemRequest,
    ) -> cloud_siem_20241212_models.CheckUpgradeItemResponse:
        """
        @summary 检查升级项
        
        @param request: CheckUpgradeItemRequest
        @return: CheckUpgradeItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_upgrade_item_with_options(request, runtime)

    async def check_upgrade_item_async(
        self,
        request: cloud_siem_20241212_models.CheckUpgradeItemRequest,
    ) -> cloud_siem_20241212_models.CheckUpgradeItemResponse:
        """
        @summary 检查升级项
        
        @param request: CheckUpgradeItemRequest
        @return: CheckUpgradeItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_upgrade_item_with_options_async(request, runtime)

    def create_data_ingestion_with_options(
        self,
        request: cloud_siem_20241212_models.CreateDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateDataIngestionResponse:
        """
        @summary 创建数据源
        
        @param request: CreateDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity_count):
            body['CapacityCount'] = request.capacity_count
        if not UtilClient.is_unset(request.data_ingestion_mode):
            body['DataIngestionMode'] = request.data_ingestion_mode
        if not UtilClient.is_unset(request.data_ingestion_state_code):
            body['DataIngestionStateCode'] = request.data_ingestion_state_code
        if not UtilClient.is_unset(request.data_ingestion_type):
            body['DataIngestionType'] = request.data_ingestion_type
        if not UtilClient.is_unset(request.data_source_editable):
            body['DataSourceEditable'] = request.data_source_editable
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_editable):
            body['NormalizationRuleEditable'] = request.normalization_rule_editable
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.scan_data_source_id):
            body['ScanDataSourceId'] = request.scan_data_source_id
        if not UtilClient.is_unset(request.stream_job_id):
            body['StreamJobId'] = request.stream_job_id
        if not UtilClient.is_unset(request.update_time):
            body['UpdateTime'] = request.update_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_ingestion_with_options_async(
        self,
        request: cloud_siem_20241212_models.CreateDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateDataIngestionResponse:
        """
        @summary 创建数据源
        
        @param request: CreateDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity_count):
            body['CapacityCount'] = request.capacity_count
        if not UtilClient.is_unset(request.data_ingestion_mode):
            body['DataIngestionMode'] = request.data_ingestion_mode
        if not UtilClient.is_unset(request.data_ingestion_state_code):
            body['DataIngestionStateCode'] = request.data_ingestion_state_code
        if not UtilClient.is_unset(request.data_ingestion_type):
            body['DataIngestionType'] = request.data_ingestion_type
        if not UtilClient.is_unset(request.data_source_editable):
            body['DataSourceEditable'] = request.data_source_editable
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_editable):
            body['NormalizationRuleEditable'] = request.normalization_rule_editable
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.scan_data_source_id):
            body['ScanDataSourceId'] = request.scan_data_source_id
        if not UtilClient.is_unset(request.stream_job_id):
            body['StreamJobId'] = request.stream_job_id
        if not UtilClient.is_unset(request.update_time):
            body['UpdateTime'] = request.update_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_ingestion(
        self,
        request: cloud_siem_20241212_models.CreateDataIngestionRequest,
    ) -> cloud_siem_20241212_models.CreateDataIngestionResponse:
        """
        @summary 创建数据源
        
        @param request: CreateDataIngestionRequest
        @return: CreateDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_ingestion_with_options(request, runtime)

    async def create_data_ingestion_async(
        self,
        request: cloud_siem_20241212_models.CreateDataIngestionRequest,
    ) -> cloud_siem_20241212_models.CreateDataIngestionResponse:
        """
        @summary 创建数据源
        
        @param request: CreateDataIngestionRequest
        @return: CreateDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_ingestion_with_options_async(request, runtime)

    def create_data_set_with_options(
        self,
        request: cloud_siem_20241212_models.CreateDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateDataSetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_description):
            body['DataSetDescription'] = request.data_set_description
        if not UtilClient.is_unset(request.data_set_field_key_name):
            body['DataSetFieldKeyName'] = request.data_set_field_key_name
        if not UtilClient.is_unset(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not UtilClient.is_unset(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not UtilClient.is_unset(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        if not UtilClient.is_unset(request.data_set_type):
            body['DataSetType'] = request.data_set_type
        body_flat = {}
        if not UtilClient.is_unset(request.ip_whitelist_recognizers):
            body_flat['IpWhitelistRecognizers'] = request.ip_whitelist_recognizers
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSet',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_set_with_options_async(
        self,
        request: cloud_siem_20241212_models.CreateDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateDataSetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_description):
            body['DataSetDescription'] = request.data_set_description
        if not UtilClient.is_unset(request.data_set_field_key_name):
            body['DataSetFieldKeyName'] = request.data_set_field_key_name
        if not UtilClient.is_unset(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not UtilClient.is_unset(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not UtilClient.is_unset(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        if not UtilClient.is_unset(request.data_set_type):
            body['DataSetType'] = request.data_set_type
        body_flat = {}
        if not UtilClient.is_unset(request.ip_whitelist_recognizers):
            body_flat['IpWhitelistRecognizers'] = request.ip_whitelist_recognizers
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSet',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_set(
        self,
        request: cloud_siem_20241212_models.CreateDataSetRequest,
    ) -> cloud_siem_20241212_models.CreateDataSetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDataSetRequest
        @return: CreateDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_set_with_options(request, runtime)

    async def create_data_set_async(
        self,
        request: cloud_siem_20241212_models.CreateDataSetRequest,
    ) -> cloud_siem_20241212_models.CreateDataSetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDataSetRequest
        @return: CreateDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_set_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateDataSourceResponse:
        """
        @summary 创建数据源
        
        @param tmp_req: CreateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.CreateDataSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.data_source_references):
            request.data_source_references_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_references, 'DataSourceReferences', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        if not UtilClient.is_unset(request.data_source_recognizer):
            body['DataSourceRecognizer'] = request.data_source_recognizer
        if not UtilClient.is_unset(request.data_source_references_shrink):
            body['DataSourceReferences'] = request.data_source_references_shrink
        body_flat = {}
        if not UtilClient.is_unset(request.data_source_stores):
            body_flat['DataSourceStores'] = request.data_source_stores
        if not UtilClient.is_unset(request.data_source_template_id):
            body['DataSourceTemplateId'] = request.data_source_template_id
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.update_time):
            body['UpdateTime'] = request.update_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateDataSourceResponse:
        """
        @summary 创建数据源
        
        @param tmp_req: CreateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.CreateDataSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.data_source_references):
            request.data_source_references_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_references, 'DataSourceReferences', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        if not UtilClient.is_unset(request.data_source_recognizer):
            body['DataSourceRecognizer'] = request.data_source_recognizer
        if not UtilClient.is_unset(request.data_source_references_shrink):
            body['DataSourceReferences'] = request.data_source_references_shrink
        body_flat = {}
        if not UtilClient.is_unset(request.data_source_stores):
            body_flat['DataSourceStores'] = request.data_source_stores
        if not UtilClient.is_unset(request.data_source_template_id):
            body['DataSourceTemplateId'] = request.data_source_template_id
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.update_time):
            body['UpdateTime'] = request.update_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source(
        self,
        request: cloud_siem_20241212_models.CreateDataSourceRequest,
    ) -> cloud_siem_20241212_models.CreateDataSourceResponse:
        """
        @summary 创建数据源
        
        @param request: CreateDataSourceRequest
        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: cloud_siem_20241212_models.CreateDataSourceRequest,
    ) -> cloud_siem_20241212_models.CreateDataSourceResponse:
        """
        @summary 创建数据源
        
        @param request: CreateDataSourceRequest
        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_detection_rule_with_options(
        self,
        request: cloud_siem_20241212_models.CreateDetectionRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateDetectionRuleResponse:
        """
        @summary 创建检测规则
        
        @param request: CreateDetectionRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDetectionRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not UtilClient.is_unset(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_schema_id):
            body['AlertSchemaId'] = request.alert_schema_id
        if not UtilClient.is_unset(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not UtilClient.is_unset(request.alert_threshold_count):
            body['AlertThresholdCount'] = request.alert_threshold_count
        if not UtilClient.is_unset(request.alert_threshold_group):
            body['AlertThresholdGroup'] = request.alert_threshold_group
        if not UtilClient.is_unset(request.alert_threshold_period):
            body['AlertThresholdPeriod'] = request.alert_threshold_period
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.detection_expression_content):
            body['DetectionExpressionContent'] = request.detection_expression_content
        if not UtilClient.is_unset(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not UtilClient.is_unset(request.detection_rule_description):
            body['DetectionRuleDescription'] = request.detection_rule_description
        if not UtilClient.is_unset(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not UtilClient.is_unset(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not UtilClient.is_unset(request.detection_rule_template_id):
            body['DetectionRuleTemplateId'] = request.detection_rule_template_id
        if not UtilClient.is_unset(request.detection_rule_template_version):
            body['DetectionRuleTemplateVersion'] = request.detection_rule_template_version
        if not UtilClient.is_unset(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not UtilClient.is_unset(request.entity_mappings):
            body['EntityMappings'] = request.entity_mappings
        if not UtilClient.is_unset(request.incident_aggregation_expression):
            body['IncidentAggregationExpression'] = request.incident_aggregation_expression
        if not UtilClient.is_unset(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not UtilClient.is_unset(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not UtilClient.is_unset(request.playbook_parameters):
            body['PlaybookParameters'] = request.playbook_parameters
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.schedule_begin_time):
            body['ScheduleBeginTime'] = request.schedule_begin_time
        if not UtilClient.is_unset(request.schedule_expression):
            body['ScheduleExpression'] = request.schedule_expression
        if not UtilClient.is_unset(request.schedule_max_retries):
            body['ScheduleMaxRetries'] = request.schedule_max_retries
        if not UtilClient.is_unset(request.schedule_max_timeout):
            body['ScheduleMaxTimeout'] = request.schedule_max_timeout
        if not UtilClient.is_unset(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.schedule_window):
            body['ScheduleWindow'] = request.schedule_window
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDetectionRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateDetectionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_detection_rule_with_options_async(
        self,
        request: cloud_siem_20241212_models.CreateDetectionRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateDetectionRuleResponse:
        """
        @summary 创建检测规则
        
        @param request: CreateDetectionRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDetectionRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not UtilClient.is_unset(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_schema_id):
            body['AlertSchemaId'] = request.alert_schema_id
        if not UtilClient.is_unset(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not UtilClient.is_unset(request.alert_threshold_count):
            body['AlertThresholdCount'] = request.alert_threshold_count
        if not UtilClient.is_unset(request.alert_threshold_group):
            body['AlertThresholdGroup'] = request.alert_threshold_group
        if not UtilClient.is_unset(request.alert_threshold_period):
            body['AlertThresholdPeriod'] = request.alert_threshold_period
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.detection_expression_content):
            body['DetectionExpressionContent'] = request.detection_expression_content
        if not UtilClient.is_unset(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not UtilClient.is_unset(request.detection_rule_description):
            body['DetectionRuleDescription'] = request.detection_rule_description
        if not UtilClient.is_unset(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not UtilClient.is_unset(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not UtilClient.is_unset(request.detection_rule_template_id):
            body['DetectionRuleTemplateId'] = request.detection_rule_template_id
        if not UtilClient.is_unset(request.detection_rule_template_version):
            body['DetectionRuleTemplateVersion'] = request.detection_rule_template_version
        if not UtilClient.is_unset(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not UtilClient.is_unset(request.entity_mappings):
            body['EntityMappings'] = request.entity_mappings
        if not UtilClient.is_unset(request.incident_aggregation_expression):
            body['IncidentAggregationExpression'] = request.incident_aggregation_expression
        if not UtilClient.is_unset(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not UtilClient.is_unset(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not UtilClient.is_unset(request.playbook_parameters):
            body['PlaybookParameters'] = request.playbook_parameters
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.schedule_begin_time):
            body['ScheduleBeginTime'] = request.schedule_begin_time
        if not UtilClient.is_unset(request.schedule_expression):
            body['ScheduleExpression'] = request.schedule_expression
        if not UtilClient.is_unset(request.schedule_max_retries):
            body['ScheduleMaxRetries'] = request.schedule_max_retries
        if not UtilClient.is_unset(request.schedule_max_timeout):
            body['ScheduleMaxTimeout'] = request.schedule_max_timeout
        if not UtilClient.is_unset(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.schedule_window):
            body['ScheduleWindow'] = request.schedule_window
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDetectionRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateDetectionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_detection_rule(
        self,
        request: cloud_siem_20241212_models.CreateDetectionRuleRequest,
    ) -> cloud_siem_20241212_models.CreateDetectionRuleResponse:
        """
        @summary 创建检测规则
        
        @param request: CreateDetectionRuleRequest
        @return: CreateDetectionRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_detection_rule_with_options(request, runtime)

    async def create_detection_rule_async(
        self,
        request: cloud_siem_20241212_models.CreateDetectionRuleRequest,
    ) -> cloud_siem_20241212_models.CreateDetectionRuleResponse:
        """
        @summary 创建检测规则
        
        @param request: CreateDetectionRuleRequest
        @return: CreateDetectionRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_detection_rule_with_options_async(request, runtime)

    def create_export_task_with_options(
        self,
        request: cloud_siem_20241212_models.CreateExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.export_task_parameter):
            body['ExportTaskParameter'] = request.export_task_parameter
        if not UtilClient.is_unset(request.export_task_type):
            body['ExportTaskType'] = request.export_task_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExportTask',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_export_task_with_options_async(
        self,
        request: cloud_siem_20241212_models.CreateExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.export_task_parameter):
            body['ExportTaskParameter'] = request.export_task_parameter
        if not UtilClient.is_unset(request.export_task_type):
            body['ExportTaskType'] = request.export_task_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExportTask',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_export_task(
        self,
        request: cloud_siem_20241212_models.CreateExportTaskRequest,
    ) -> cloud_siem_20241212_models.CreateExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateExportTaskRequest
        @return: CreateExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_export_task_with_options(request, runtime)

    async def create_export_task_async(
        self,
        request: cloud_siem_20241212_models.CreateExportTaskRequest,
    ) -> cloud_siem_20241212_models.CreateExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateExportTaskRequest
        @return: CreateExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_export_task_with_options_async(request, runtime)

    def create_log_store_with_options(
        self,
        request: cloud_siem_20241212_models.CreateLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateLogStoreResponse:
        """
        @summary 创建LogStore
        
        @param request: CreateLogStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_store_with_options_async(
        self,
        request: cloud_siem_20241212_models.CreateLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateLogStoreResponse:
        """
        @summary 创建LogStore
        
        @param request: CreateLogStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_store(
        self,
        request: cloud_siem_20241212_models.CreateLogStoreRequest,
    ) -> cloud_siem_20241212_models.CreateLogStoreResponse:
        """
        @summary 创建LogStore
        
        @param request: CreateLogStoreRequest
        @return: CreateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_log_store_with_options(request, runtime)

    async def create_log_store_async(
        self,
        request: cloud_siem_20241212_models.CreateLogStoreRequest,
    ) -> cloud_siem_20241212_models.CreateLogStoreResponse:
        """
        @summary 创建LogStore
        
        @param request: CreateLogStoreRequest
        @return: CreateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_log_store_with_options_async(request, runtime)

    def create_normalization_rule_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.CreateNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateNormalizationRuleResponse:
        """
        @summary 创建标准化规则
        
        @param tmp_req: CreateNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNormalizationRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.CreateNormalizationRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not UtilClient.is_unset(request.normalization_rule_description):
            body['NormalizationRuleDescription'] = request.normalization_rule_description
        if not UtilClient.is_unset(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not UtilClient.is_unset(request.normalization_rule_format):
            body['NormalizationRuleFormat'] = request.normalization_rule_format
        if not UtilClient.is_unset(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not UtilClient.is_unset(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not UtilClient.is_unset(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not UtilClient.is_unset(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not UtilClient.is_unset(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_normalization_rule_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.CreateNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateNormalizationRuleResponse:
        """
        @summary 创建标准化规则
        
        @param tmp_req: CreateNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNormalizationRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.CreateNormalizationRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not UtilClient.is_unset(request.normalization_rule_description):
            body['NormalizationRuleDescription'] = request.normalization_rule_description
        if not UtilClient.is_unset(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not UtilClient.is_unset(request.normalization_rule_format):
            body['NormalizationRuleFormat'] = request.normalization_rule_format
        if not UtilClient.is_unset(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not UtilClient.is_unset(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not UtilClient.is_unset(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not UtilClient.is_unset(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not UtilClient.is_unset(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_normalization_rule(
        self,
        request: cloud_siem_20241212_models.CreateNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.CreateNormalizationRuleResponse:
        """
        @summary 创建标准化规则
        
        @param request: CreateNormalizationRuleRequest
        @return: CreateNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_normalization_rule_with_options(request, runtime)

    async def create_normalization_rule_async(
        self,
        request: cloud_siem_20241212_models.CreateNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.CreateNormalizationRuleResponse:
        """
        @summary 创建标准化规则
        
        @param request: CreateNormalizationRuleRequest
        @return: CreateNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_normalization_rule_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        request: cloud_siem_20241212_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateProductResponse:
        """
        @summary 创建产品
        
        @param request: CreateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: cloud_siem_20241212_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateProductResponse:
        """
        @summary 创建产品
        
        @param request: CreateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: cloud_siem_20241212_models.CreateProductRequest,
    ) -> cloud_siem_20241212_models.CreateProductResponse:
        """
        @summary 创建产品
        
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: cloud_siem_20241212_models.CreateProductRequest,
    ) -> cloud_siem_20241212_models.CreateProductResponse:
        """
        @summary 创建产品
        
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def create_vendor_with_options(
        self,
        request: cloud_siem_20241212_models.CreateVendorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateVendorResponse:
        """
        @summary 创建厂商
        
        @param request: CreateVendorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVendorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVendor',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateVendorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vendor_with_options_async(
        self,
        request: cloud_siem_20241212_models.CreateVendorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.CreateVendorResponse:
        """
        @summary 创建厂商
        
        @param request: CreateVendorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVendorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVendor',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.CreateVendorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vendor(
        self,
        request: cloud_siem_20241212_models.CreateVendorRequest,
    ) -> cloud_siem_20241212_models.CreateVendorResponse:
        """
        @summary 创建厂商
        
        @param request: CreateVendorRequest
        @return: CreateVendorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vendor_with_options(request, runtime)

    async def create_vendor_async(
        self,
        request: cloud_siem_20241212_models.CreateVendorRequest,
    ) -> cloud_siem_20241212_models.CreateVendorResponse:
        """
        @summary 创建厂商
        
        @param request: CreateVendorRequest
        @return: CreateVendorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vendor_with_options_async(request, runtime)

    def delete_data_ingestion_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDataIngestionResponse:
        """
        @summary 删除数据接入
        
        @param request: DeleteDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_ingestion_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDataIngestionResponse:
        """
        @summary 删除数据接入
        
        @param request: DeleteDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_ingestion(
        self,
        request: cloud_siem_20241212_models.DeleteDataIngestionRequest,
    ) -> cloud_siem_20241212_models.DeleteDataIngestionResponse:
        """
        @summary 删除数据接入
        
        @param request: DeleteDataIngestionRequest
        @return: DeleteDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_ingestion_with_options(request, runtime)

    async def delete_data_ingestion_async(
        self,
        request: cloud_siem_20241212_models.DeleteDataIngestionRequest,
    ) -> cloud_siem_20241212_models.DeleteDataIngestionResponse:
        """
        @summary 删除数据接入
        
        @param request: DeleteDataIngestionRequest
        @return: DeleteDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_ingestion_with_options_async(request, runtime)

    def delete_data_set_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDataSetResponse:
        """
        @summary 删除数据集
        
        @param request: DeleteDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_set_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDataSetResponse:
        """
        @summary 删除数据集
        
        @param request: DeleteDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_set(
        self,
        request: cloud_siem_20241212_models.DeleteDataSetRequest,
    ) -> cloud_siem_20241212_models.DeleteDataSetResponse:
        """
        @summary 删除数据集
        
        @param request: DeleteDataSetRequest
        @return: DeleteDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_set_with_options(request, runtime)

    async def delete_data_set_async(
        self,
        request: cloud_siem_20241212_models.DeleteDataSetRequest,
    ) -> cloud_siem_20241212_models.DeleteDataSetResponse:
        """
        @summary 删除数据集
        
        @param request: DeleteDataSetRequest
        @return: DeleteDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_set_with_options_async(request, runtime)

    def delete_data_set_record_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteDataSetRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDataSetRecordResponse:
        """
        @summary 删除数据集记录
        
        @param request: DeleteDataSetRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSetRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.data_set_record_ids):
            body['DataSetRecordIds'] = request.data_set_record_ids
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSetRecord',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDataSetRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_set_record_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteDataSetRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDataSetRecordResponse:
        """
        @summary 删除数据集记录
        
        @param request: DeleteDataSetRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSetRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.data_set_record_ids):
            body['DataSetRecordIds'] = request.data_set_record_ids
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSetRecord',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDataSetRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_set_record(
        self,
        request: cloud_siem_20241212_models.DeleteDataSetRecordRequest,
    ) -> cloud_siem_20241212_models.DeleteDataSetRecordResponse:
        """
        @summary 删除数据集记录
        
        @param request: DeleteDataSetRecordRequest
        @return: DeleteDataSetRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_set_record_with_options(request, runtime)

    async def delete_data_set_record_async(
        self,
        request: cloud_siem_20241212_models.DeleteDataSetRecordRequest,
    ) -> cloud_siem_20241212_models.DeleteDataSetRecordResponse:
        """
        @summary 删除数据集记录
        
        @param request: DeleteDataSetRecordRequest
        @return: DeleteDataSetRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_set_record_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: cloud_siem_20241212_models.DeleteDataSourceRequest,
    ) -> cloud_siem_20241212_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: cloud_siem_20241212_models.DeleteDataSourceRequest,
    ) -> cloud_siem_20241212_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_detection_rule_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteDetectionRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDetectionRuleResponse:
        """
        @summary 删除检测规则
        
        @param request: DeleteDetectionRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDetectionRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDetectionRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDetectionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_detection_rule_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteDetectionRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteDetectionRuleResponse:
        """
        @summary 删除检测规则
        
        @param request: DeleteDetectionRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDetectionRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDetectionRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteDetectionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_detection_rule(
        self,
        request: cloud_siem_20241212_models.DeleteDetectionRuleRequest,
    ) -> cloud_siem_20241212_models.DeleteDetectionRuleResponse:
        """
        @summary 删除检测规则
        
        @param request: DeleteDetectionRuleRequest
        @return: DeleteDetectionRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_detection_rule_with_options(request, runtime)

    async def delete_detection_rule_async(
        self,
        request: cloud_siem_20241212_models.DeleteDetectionRuleRequest,
    ) -> cloud_siem_20241212_models.DeleteDetectionRuleResponse:
        """
        @summary 删除检测规则
        
        @param request: DeleteDetectionRuleRequest
        @return: DeleteDetectionRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_detection_rule_with_options_async(request, runtime)

    def delete_log_store_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteLogStoreResponse:
        """
        @summary 删除LogStore
        
        @param request: DeleteLogStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLogStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLogStore',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_store_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteLogStoreResponse:
        """
        @summary 删除LogStore
        
        @param request: DeleteLogStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLogStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLogStore',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_store(
        self,
        request: cloud_siem_20241212_models.DeleteLogStoreRequest,
    ) -> cloud_siem_20241212_models.DeleteLogStoreResponse:
        """
        @summary 删除LogStore
        
        @param request: DeleteLogStoreRequest
        @return: DeleteLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_log_store_with_options(request, runtime)

    async def delete_log_store_async(
        self,
        request: cloud_siem_20241212_models.DeleteLogStoreRequest,
    ) -> cloud_siem_20241212_models.DeleteLogStoreResponse:
        """
        @summary 删除LogStore
        
        @param request: DeleteLogStoreRequest
        @return: DeleteLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_log_store_with_options_async(request, runtime)

    def delete_normalization_rule_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteNormalizationRuleResponse:
        """
        @summary 删除标准化规则
        
        @param request: DeleteNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNormalizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_normalization_rule_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteNormalizationRuleResponse:
        """
        @summary 删除标准化规则
        
        @param request: DeleteNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNormalizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_normalization_rule(
        self,
        request: cloud_siem_20241212_models.DeleteNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.DeleteNormalizationRuleResponse:
        """
        @summary 删除标准化规则
        
        @param request: DeleteNormalizationRuleRequest
        @return: DeleteNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_normalization_rule_with_options(request, runtime)

    async def delete_normalization_rule_async(
        self,
        request: cloud_siem_20241212_models.DeleteNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.DeleteNormalizationRuleResponse:
        """
        @summary 删除标准化规则
        
        @param request: DeleteNormalizationRuleRequest
        @return: DeleteNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_normalization_rule_with_options_async(request, runtime)

    def delete_normalization_rule_version_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteNormalizationRuleVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteNormalizationRuleVersionResponse:
        """
        @summary 删除标准化规则版本
        
        @param request: DeleteNormalizationRuleVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNormalizationRuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNormalizationRuleVersion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteNormalizationRuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_normalization_rule_version_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteNormalizationRuleVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteNormalizationRuleVersionResponse:
        """
        @summary 删除标准化规则版本
        
        @param request: DeleteNormalizationRuleVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNormalizationRuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNormalizationRuleVersion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteNormalizationRuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_normalization_rule_version(
        self,
        request: cloud_siem_20241212_models.DeleteNormalizationRuleVersionRequest,
    ) -> cloud_siem_20241212_models.DeleteNormalizationRuleVersionResponse:
        """
        @summary 删除标准化规则版本
        
        @param request: DeleteNormalizationRuleVersionRequest
        @return: DeleteNormalizationRuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_normalization_rule_version_with_options(request, runtime)

    async def delete_normalization_rule_version_async(
        self,
        request: cloud_siem_20241212_models.DeleteNormalizationRuleVersionRequest,
    ) -> cloud_siem_20241212_models.DeleteNormalizationRuleVersionResponse:
        """
        @summary 删除标准化规则版本
        
        @param request: DeleteNormalizationRuleVersionRequest
        @return: DeleteNormalizationRuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_normalization_rule_version_with_options_async(request, runtime)

    def delete_product_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteProductResponse:
        """
        @summary 删除产品
        
        @param request: DeleteProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteProductResponse:
        """
        @summary 删除产品
        
        @param request: DeleteProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product(
        self,
        request: cloud_siem_20241212_models.DeleteProductRequest,
    ) -> cloud_siem_20241212_models.DeleteProductResponse:
        """
        @summary 删除产品
        
        @param request: DeleteProductRequest
        @return: DeleteProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    async def delete_product_async(
        self,
        request: cloud_siem_20241212_models.DeleteProductRequest,
    ) -> cloud_siem_20241212_models.DeleteProductResponse:
        """
        @summary 删除产品
        
        @param request: DeleteProductRequest
        @return: DeleteProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_product_with_options_async(request, runtime)

    def delete_vendor_with_options(
        self,
        request: cloud_siem_20241212_models.DeleteVendorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteVendorResponse:
        """
        @summary 删除厂商
        
        @param request: DeleteVendorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVendorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVendor',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteVendorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vendor_with_options_async(
        self,
        request: cloud_siem_20241212_models.DeleteVendorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DeleteVendorResponse:
        """
        @summary 删除厂商
        
        @param request: DeleteVendorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVendorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVendor',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DeleteVendorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vendor(
        self,
        request: cloud_siem_20241212_models.DeleteVendorRequest,
    ) -> cloud_siem_20241212_models.DeleteVendorResponse:
        """
        @summary 删除厂商
        
        @param request: DeleteVendorRequest
        @return: DeleteVendorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vendor_with_options(request, runtime)

    async def delete_vendor_async(
        self,
        request: cloud_siem_20241212_models.DeleteVendorRequest,
    ) -> cloud_siem_20241212_models.DeleteVendorResponse:
        """
        @summary 删除厂商
        
        @param request: DeleteVendorRequest
        @return: DeleteVendorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vendor_with_options_async(request, runtime)

    def disable_data_ingestion_with_options(
        self,
        request: cloud_siem_20241212_models.DisableDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DisableDataIngestionResponse:
        """
        @summary 停止数据接入
        
        @param request: DisableDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DisableDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_data_ingestion_with_options_async(
        self,
        request: cloud_siem_20241212_models.DisableDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.DisableDataIngestionResponse:
        """
        @summary 停止数据接入
        
        @param request: DisableDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.DisableDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_data_ingestion(
        self,
        request: cloud_siem_20241212_models.DisableDataIngestionRequest,
    ) -> cloud_siem_20241212_models.DisableDataIngestionResponse:
        """
        @summary 停止数据接入
        
        @param request: DisableDataIngestionRequest
        @return: DisableDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_data_ingestion_with_options(request, runtime)

    async def disable_data_ingestion_async(
        self,
        request: cloud_siem_20241212_models.DisableDataIngestionRequest,
    ) -> cloud_siem_20241212_models.DisableDataIngestionResponse:
        """
        @summary 停止数据接入
        
        @param request: DisableDataIngestionRequest
        @return: DisableDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_data_ingestion_with_options_async(request, runtime)

    def enable_data_ingestion_with_options(
        self,
        request: cloud_siem_20241212_models.EnableDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.EnableDataIngestionResponse:
        """
        @summary 启动数据接入
        
        @param request: EnableDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.EnableDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_data_ingestion_with_options_async(
        self,
        request: cloud_siem_20241212_models.EnableDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.EnableDataIngestionResponse:
        """
        @summary 启动数据接入
        
        @param request: EnableDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.EnableDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_data_ingestion(
        self,
        request: cloud_siem_20241212_models.EnableDataIngestionRequest,
    ) -> cloud_siem_20241212_models.EnableDataIngestionResponse:
        """
        @summary 启动数据接入
        
        @param request: EnableDataIngestionRequest
        @return: EnableDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_data_ingestion_with_options(request, runtime)

    async def enable_data_ingestion_async(
        self,
        request: cloud_siem_20241212_models.EnableDataIngestionRequest,
    ) -> cloud_siem_20241212_models.EnableDataIngestionResponse:
        """
        @summary 启动数据接入
        
        @param request: EnableDataIngestionRequest
        @return: EnableDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_data_ingestion_with_options_async(request, runtime)

    def execute_log_query_with_options(
        self,
        request: cloud_siem_20241212_models.ExecuteLogQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ExecuteLogQueryResponse:
        """
        @summary 查看LogStore
        
        @param request: ExecuteLogQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteLogQueryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_query):
            body['LogQuery'] = request.log_query
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteLogQuery',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ExecuteLogQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_log_query_with_options_async(
        self,
        request: cloud_siem_20241212_models.ExecuteLogQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ExecuteLogQueryResponse:
        """
        @summary 查看LogStore
        
        @param request: ExecuteLogQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteLogQueryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_query):
            body['LogQuery'] = request.log_query
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteLogQuery',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ExecuteLogQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_log_query(
        self,
        request: cloud_siem_20241212_models.ExecuteLogQueryRequest,
    ) -> cloud_siem_20241212_models.ExecuteLogQueryResponse:
        """
        @summary 查看LogStore
        
        @param request: ExecuteLogQueryRequest
        @return: ExecuteLogQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_log_query_with_options(request, runtime)

    async def execute_log_query_async(
        self,
        request: cloud_siem_20241212_models.ExecuteLogQueryRequest,
    ) -> cloud_siem_20241212_models.ExecuteLogQueryResponse:
        """
        @summary 查看LogStore
        
        @param request: ExecuteLogQueryRequest
        @return: ExecuteLogQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_log_query_with_options_async(request, runtime)

    def execute_upgrade_with_options(
        self,
        request: cloud_siem_20241212_models.ExecuteUpgradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ExecuteUpgradeResponse:
        """
        @summary 执行升级
        
        @param request: ExecuteUpgradeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteUpgradeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteUpgrade',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ExecuteUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_upgrade_with_options_async(
        self,
        request: cloud_siem_20241212_models.ExecuteUpgradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ExecuteUpgradeResponse:
        """
        @summary 执行升级
        
        @param request: ExecuteUpgradeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteUpgradeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteUpgrade',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ExecuteUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_upgrade(
        self,
        request: cloud_siem_20241212_models.ExecuteUpgradeRequest,
    ) -> cloud_siem_20241212_models.ExecuteUpgradeResponse:
        """
        @summary 执行升级
        
        @param request: ExecuteUpgradeRequest
        @return: ExecuteUpgradeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_upgrade_with_options(request, runtime)

    async def execute_upgrade_async(
        self,
        request: cloud_siem_20241212_models.ExecuteUpgradeRequest,
    ) -> cloud_siem_20241212_models.ExecuteUpgradeResponse:
        """
        @summary 执行升级
        
        @param request: ExecuteUpgradeRequest
        @return: ExecuteUpgradeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_upgrade_with_options_async(request, runtime)

    def get_data_batch_ingestion_with_options(
        self,
        request: cloud_siem_20241212_models.GetDataBatchIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetDataBatchIngestionResponse:
        """
        @summary 获取数据批量接入
        
        @param request: GetDataBatchIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataBatchIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataBatchIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetDataBatchIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_batch_ingestion_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetDataBatchIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetDataBatchIngestionResponse:
        """
        @summary 获取数据批量接入
        
        @param request: GetDataBatchIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataBatchIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataBatchIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetDataBatchIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_batch_ingestion(
        self,
        request: cloud_siem_20241212_models.GetDataBatchIngestionRequest,
    ) -> cloud_siem_20241212_models.GetDataBatchIngestionResponse:
        """
        @summary 获取数据批量接入
        
        @param request: GetDataBatchIngestionRequest
        @return: GetDataBatchIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_batch_ingestion_with_options(request, runtime)

    async def get_data_batch_ingestion_async(
        self,
        request: cloud_siem_20241212_models.GetDataBatchIngestionRequest,
    ) -> cloud_siem_20241212_models.GetDataBatchIngestionResponse:
        """
        @summary 获取数据批量接入
        
        @param request: GetDataBatchIngestionRequest
        @return: GetDataBatchIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_batch_ingestion_with_options_async(request, runtime)

    def get_data_storage_with_options(
        self,
        request: cloud_siem_20241212_models.GetDataStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetDataStorageResponse:
        """
        @summary 获取日志管理页面里用户数据存储的详情。
        
        @param request: GetDataStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataStorage',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetDataStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_storage_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetDataStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetDataStorageResponse:
        """
        @summary 获取日志管理页面里用户数据存储的详情。
        
        @param request: GetDataStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataStorage',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetDataStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_storage(
        self,
        request: cloud_siem_20241212_models.GetDataStorageRequest,
    ) -> cloud_siem_20241212_models.GetDataStorageResponse:
        """
        @summary 获取日志管理页面里用户数据存储的详情。
        
        @param request: GetDataStorageRequest
        @return: GetDataStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_storage_with_options(request, runtime)

    async def get_data_storage_async(
        self,
        request: cloud_siem_20241212_models.GetDataStorageRequest,
    ) -> cloud_siem_20241212_models.GetDataStorageResponse:
        """
        @summary 获取日志管理页面里用户数据存储的详情。
        
        @param request: GetDataStorageRequest
        @return: GetDataStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_storage_with_options_async(request, runtime)

    def get_detection_statistic_with_options(
        self,
        request: cloud_siem_20241212_models.GetDetectionStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetDetectionStatisticResponse:
        """
        @summary 更新检测规则
        
        @param request: GetDetectionStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDetectionStatisticResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectionStatistic',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetDetectionStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detection_statistic_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetDetectionStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetDetectionStatisticResponse:
        """
        @summary 更新检测规则
        
        @param request: GetDetectionStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDetectionStatisticResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetectionStatistic',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetDetectionStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detection_statistic(
        self,
        request: cloud_siem_20241212_models.GetDetectionStatisticRequest,
    ) -> cloud_siem_20241212_models.GetDetectionStatisticResponse:
        """
        @summary 更新检测规则
        
        @param request: GetDetectionStatisticRequest
        @return: GetDetectionStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_detection_statistic_with_options(request, runtime)

    async def get_detection_statistic_async(
        self,
        request: cloud_siem_20241212_models.GetDetectionStatisticRequest,
    ) -> cloud_siem_20241212_models.GetDetectionStatisticResponse:
        """
        @summary 更新检测规则
        
        @param request: GetDetectionStatisticRequest
        @return: GetDetectionStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_detection_statistic_with_options_async(request, runtime)

    def get_export_task_with_options(
        self,
        request: cloud_siem_20241212_models.GetExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetExportTaskResponse:
        """
        @summary 获取导出任务进度
        
        @param request: GetExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.export_id):
            body['ExportId'] = request.export_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExportTask',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_export_task_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetExportTaskResponse:
        """
        @summary 获取导出任务进度
        
        @param request: GetExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.export_id):
            body['ExportId'] = request.export_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExportTask',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_export_task(
        self,
        request: cloud_siem_20241212_models.GetExportTaskRequest,
    ) -> cloud_siem_20241212_models.GetExportTaskResponse:
        """
        @summary 获取导出任务进度
        
        @param request: GetExportTaskRequest
        @return: GetExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_export_task_with_options(request, runtime)

    async def get_export_task_async(
        self,
        request: cloud_siem_20241212_models.GetExportTaskRequest,
    ) -> cloud_siem_20241212_models.GetExportTaskResponse:
        """
        @summary 获取导出任务进度
        
        @param request: GetExportTaskRequest
        @return: GetExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_export_task_with_options_async(request, runtime)

    def get_incident_with_options(
        self,
        request: cloud_siem_20241212_models.GetIncidentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetIncidentResponse:
        """
        @summary 获取事件列表
        
        @param request: GetIncidentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIncidentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncident',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_incident_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetIncidentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetIncidentResponse:
        """
        @summary 获取事件列表
        
        @param request: GetIncidentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIncidentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncident',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_incident(
        self,
        request: cloud_siem_20241212_models.GetIncidentRequest,
    ) -> cloud_siem_20241212_models.GetIncidentResponse:
        """
        @summary 获取事件列表
        
        @param request: GetIncidentRequest
        @return: GetIncidentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_incident_with_options(request, runtime)

    async def get_incident_async(
        self,
        request: cloud_siem_20241212_models.GetIncidentRequest,
    ) -> cloud_siem_20241212_models.GetIncidentResponse:
        """
        @summary 获取事件列表
        
        @param request: GetIncidentRequest
        @return: GetIncidentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_incident_with_options_async(request, runtime)

    def get_log_ticket_with_options(
        self,
        request: cloud_siem_20241212_models.GetLogTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetLogTicketResponse:
        """
        @summary 查看LogStore
        
        @param request: GetLogTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogTicket',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetLogTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_ticket_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetLogTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetLogTicketResponse:
        """
        @summary 查看LogStore
        
        @param request: GetLogTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogTicket',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetLogTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_ticket(
        self,
        request: cloud_siem_20241212_models.GetLogTicketRequest,
    ) -> cloud_siem_20241212_models.GetLogTicketResponse:
        """
        @summary 查看LogStore
        
        @param request: GetLogTicketRequest
        @return: GetLogTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_log_ticket_with_options(request, runtime)

    async def get_log_ticket_async(
        self,
        request: cloud_siem_20241212_models.GetLogTicketRequest,
    ) -> cloud_siem_20241212_models.GetLogTicketResponse:
        """
        @summary 查看LogStore
        
        @param request: GetLogTicketRequest
        @return: GetLogTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_log_ticket_with_options_async(request, runtime)

    def get_normalization_rule_with_options(
        self,
        request: cloud_siem_20241212_models.GetNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetNormalizationRuleResponse:
        """
        @summary 获取标准化规则
        
        @param request: GetNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNormalizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_normalization_rule_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetNormalizationRuleResponse:
        """
        @summary 获取标准化规则
        
        @param request: GetNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNormalizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_normalization_rule(
        self,
        request: cloud_siem_20241212_models.GetNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.GetNormalizationRuleResponse:
        """
        @summary 获取标准化规则
        
        @param request: GetNormalizationRuleRequest
        @return: GetNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_normalization_rule_with_options(request, runtime)

    async def get_normalization_rule_async(
        self,
        request: cloud_siem_20241212_models.GetNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.GetNormalizationRuleResponse:
        """
        @summary 获取标准化规则
        
        @param request: GetNormalizationRuleRequest
        @return: GetNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_normalization_rule_with_options_async(request, runtime)

    def get_normalization_rule_version_with_options(
        self,
        request: cloud_siem_20241212_models.GetNormalizationRuleVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetNormalizationRuleVersionResponse:
        """
        @summary 获取标准化规则指定版本信息
        
        @param request: GetNormalizationRuleVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNormalizationRuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNormalizationRuleVersion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetNormalizationRuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_normalization_rule_version_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetNormalizationRuleVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetNormalizationRuleVersionResponse:
        """
        @summary 获取标准化规则指定版本信息
        
        @param request: GetNormalizationRuleVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNormalizationRuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNormalizationRuleVersion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetNormalizationRuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_normalization_rule_version(
        self,
        request: cloud_siem_20241212_models.GetNormalizationRuleVersionRequest,
    ) -> cloud_siem_20241212_models.GetNormalizationRuleVersionResponse:
        """
        @summary 获取标准化规则指定版本信息
        
        @param request: GetNormalizationRuleVersionRequest
        @return: GetNormalizationRuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_normalization_rule_version_with_options(request, runtime)

    async def get_normalization_rule_version_async(
        self,
        request: cloud_siem_20241212_models.GetNormalizationRuleVersionRequest,
    ) -> cloud_siem_20241212_models.GetNormalizationRuleVersionResponse:
        """
        @summary 获取标准化规则指定版本信息
        
        @param request: GetNormalizationRuleVersionRequest
        @return: GetNormalizationRuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_normalization_rule_version_with_options_async(request, runtime)

    def get_normalization_schema_with_options(
        self,
        request: cloud_siem_20241212_models.GetNormalizationSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetNormalizationSchemaResponse:
        """
        @summary 获取Schema信息以及字段
        
        @param request: GetNormalizationSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNormalizationSchemaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNormalizationSchema',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetNormalizationSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_normalization_schema_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetNormalizationSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetNormalizationSchemaResponse:
        """
        @summary 获取Schema信息以及字段
        
        @param request: GetNormalizationSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNormalizationSchemaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNormalizationSchema',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetNormalizationSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_normalization_schema(
        self,
        request: cloud_siem_20241212_models.GetNormalizationSchemaRequest,
    ) -> cloud_siem_20241212_models.GetNormalizationSchemaResponse:
        """
        @summary 获取Schema信息以及字段
        
        @param request: GetNormalizationSchemaRequest
        @return: GetNormalizationSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_normalization_schema_with_options(request, runtime)

    async def get_normalization_schema_async(
        self,
        request: cloud_siem_20241212_models.GetNormalizationSchemaRequest,
    ) -> cloud_siem_20241212_models.GetNormalizationSchemaResponse:
        """
        @summary 获取Schema信息以及字段
        
        @param request: GetNormalizationSchemaRequest
        @return: GetNormalizationSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_normalization_schema_with_options_async(request, runtime)

    def get_user_config_with_options(
        self,
        request: cloud_siem_20241212_models.GetUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetUserConfigResponse:
        """
        @summary 获取用户配置信息
        
        @param request: GetUserConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserConfig',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_config_with_options_async(
        self,
        request: cloud_siem_20241212_models.GetUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.GetUserConfigResponse:
        """
        @summary 获取用户配置信息
        
        @param request: GetUserConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserConfig',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.GetUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_config(
        self,
        request: cloud_siem_20241212_models.GetUserConfigRequest,
    ) -> cloud_siem_20241212_models.GetUserConfigResponse:
        """
        @summary 获取用户配置信息
        
        @param request: GetUserConfigRequest
        @return: GetUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_config_with_options(request, runtime)

    async def get_user_config_async(
        self,
        request: cloud_siem_20241212_models.GetUserConfigRequest,
    ) -> cloud_siem_20241212_models.GetUserConfigResponse:
        """
        @summary 获取用户配置信息
        
        @param request: GetUserConfigRequest
        @return: GetUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_config_with_options_async(request, runtime)

    def list_data_ingestion_templates_with_options(
        self,
        request: cloud_siem_20241212_models.ListDataIngestionTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataIngestionTemplatesResponse:
        """
        @summary 查询接入模板
        
        @param request: ListDataIngestionTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataIngestionTemplatesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_template_status):
            body['DataIngestionTemplateStatus'] = request.data_ingestion_template_status
        if not UtilClient.is_unset(request.data_source_template_ids):
            body['DataSourceTemplateIds'] = request.data_source_template_ids
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataIngestionTemplates',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataIngestionTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_ingestion_templates_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListDataIngestionTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataIngestionTemplatesResponse:
        """
        @summary 查询接入模板
        
        @param request: ListDataIngestionTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataIngestionTemplatesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_template_status):
            body['DataIngestionTemplateStatus'] = request.data_ingestion_template_status
        if not UtilClient.is_unset(request.data_source_template_ids):
            body['DataSourceTemplateIds'] = request.data_source_template_ids
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataIngestionTemplates',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataIngestionTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_ingestion_templates(
        self,
        request: cloud_siem_20241212_models.ListDataIngestionTemplatesRequest,
    ) -> cloud_siem_20241212_models.ListDataIngestionTemplatesResponse:
        """
        @summary 查询接入模板
        
        @param request: ListDataIngestionTemplatesRequest
        @return: ListDataIngestionTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_ingestion_templates_with_options(request, runtime)

    async def list_data_ingestion_templates_async(
        self,
        request: cloud_siem_20241212_models.ListDataIngestionTemplatesRequest,
    ) -> cloud_siem_20241212_models.ListDataIngestionTemplatesResponse:
        """
        @summary 查询接入模板
        
        @param request: ListDataIngestionTemplatesRequest
        @return: ListDataIngestionTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_ingestion_templates_with_options_async(request, runtime)

    def list_data_ingestions_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListDataIngestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataIngestionsResponse:
        """
        @summary 获取数据接入任务列表
        
        @param tmp_req: ListDataIngestionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataIngestionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDataIngestionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_ingestion_ids):
            request.data_ingestion_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ingestion_ids, 'DataIngestionIds', 'simple')
        if not UtilClient.is_unset(tmp_req.data_ingestion_template_ids):
            request.data_ingestion_template_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ingestion_template_ids, 'DataIngestionTemplateIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_ids_shrink):
            body['DataIngestionIds'] = request.data_ingestion_ids_shrink
        if not UtilClient.is_unset(request.data_ingestion_status):
            body['DataIngestionStatus'] = request.data_ingestion_status
        if not UtilClient.is_unset(request.data_ingestion_template_ids_shrink):
            body['DataIngestionTemplateIds'] = request.data_ingestion_template_ids_shrink
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataIngestions',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataIngestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_ingestions_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListDataIngestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataIngestionsResponse:
        """
        @summary 获取数据接入任务列表
        
        @param tmp_req: ListDataIngestionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataIngestionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDataIngestionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_ingestion_ids):
            request.data_ingestion_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ingestion_ids, 'DataIngestionIds', 'simple')
        if not UtilClient.is_unset(tmp_req.data_ingestion_template_ids):
            request.data_ingestion_template_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ingestion_template_ids, 'DataIngestionTemplateIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_ids_shrink):
            body['DataIngestionIds'] = request.data_ingestion_ids_shrink
        if not UtilClient.is_unset(request.data_ingestion_status):
            body['DataIngestionStatus'] = request.data_ingestion_status
        if not UtilClient.is_unset(request.data_ingestion_template_ids_shrink):
            body['DataIngestionTemplateIds'] = request.data_ingestion_template_ids_shrink
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataIngestions',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataIngestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_ingestions(
        self,
        request: cloud_siem_20241212_models.ListDataIngestionsRequest,
    ) -> cloud_siem_20241212_models.ListDataIngestionsResponse:
        """
        @summary 获取数据接入任务列表
        
        @param request: ListDataIngestionsRequest
        @return: ListDataIngestionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_ingestions_with_options(request, runtime)

    async def list_data_ingestions_async(
        self,
        request: cloud_siem_20241212_models.ListDataIngestionsRequest,
    ) -> cloud_siem_20241212_models.ListDataIngestionsResponse:
        """
        @summary 获取数据接入任务列表
        
        @param request: ListDataIngestionsRequest
        @return: ListDataIngestionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_ingestions_with_options_async(request, runtime)

    def list_data_set_records_with_options(
        self,
        request: cloud_siem_20241212_models.ListDataSetRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataSetRecordsResponse:
        """
        @summary 获取数据集记录列表
        
        @param request: ListDataSetRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetRecordsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSetRecords',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataSetRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_records_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListDataSetRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataSetRecordsResponse:
        """
        @summary 获取数据集记录列表
        
        @param request: ListDataSetRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetRecordsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSetRecords',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataSetRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set_records(
        self,
        request: cloud_siem_20241212_models.ListDataSetRecordsRequest,
    ) -> cloud_siem_20241212_models.ListDataSetRecordsResponse:
        """
        @summary 获取数据集记录列表
        
        @param request: ListDataSetRecordsRequest
        @return: ListDataSetRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_set_records_with_options(request, runtime)

    async def list_data_set_records_async(
        self,
        request: cloud_siem_20241212_models.ListDataSetRecordsRequest,
    ) -> cloud_siem_20241212_models.ListDataSetRecordsResponse:
        """
        @summary 获取数据集记录列表
        
        @param request: ListDataSetRecordsRequest
        @return: ListDataSetRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_set_records_with_options_async(request, runtime)

    def list_data_sets_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListDataSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataSetsResponse:
        """
        @summary 获取数据集列表
        
        @param tmp_req: ListDataSetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDataSetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_set_ids):
            request.data_set_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_set_ids, 'DataSetIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.data_set_ids_shrink):
            body['DataSetIds'] = request.data_set_ids_shrink
        if not UtilClient.is_unset(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not UtilClient.is_unset(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        if not UtilClient.is_unset(request.data_set_type):
            body['DataSetType'] = request.data_set_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSets',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sets_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListDataSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataSetsResponse:
        """
        @summary 获取数据集列表
        
        @param tmp_req: ListDataSetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDataSetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_set_ids):
            request.data_set_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_set_ids, 'DataSetIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.data_set_ids_shrink):
            body['DataSetIds'] = request.data_set_ids_shrink
        if not UtilClient.is_unset(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not UtilClient.is_unset(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        if not UtilClient.is_unset(request.data_set_type):
            body['DataSetType'] = request.data_set_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSets',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sets(
        self,
        request: cloud_siem_20241212_models.ListDataSetsRequest,
    ) -> cloud_siem_20241212_models.ListDataSetsResponse:
        """
        @summary 获取数据集列表
        
        @param request: ListDataSetsRequest
        @return: ListDataSetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_sets_with_options(request, runtime)

    async def list_data_sets_async(
        self,
        request: cloud_siem_20241212_models.ListDataSetsRequest,
    ) -> cloud_siem_20241212_models.ListDataSetsResponse:
        """
        @summary 获取数据集列表
        
        @param request: ListDataSetsRequest
        @return: ListDataSetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_sets_with_options_async(request, runtime)

    def list_data_source_templates_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListDataSourceTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataSourceTemplatesResponse:
        """
        @summary 查询数据源模板
        
        @param tmp_req: ListDataSourceTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDataSourceTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_template_ids):
            request.data_source_template_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_template_ids, 'DataSourceTemplateIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.data_source_template_ids_shrink):
            body['DataSourceTemplateIds'] = request.data_source_template_ids_shrink
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSourceTemplates',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataSourceTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_templates_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListDataSourceTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataSourceTemplatesResponse:
        """
        @summary 查询数据源模板
        
        @param tmp_req: ListDataSourceTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDataSourceTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_template_ids):
            request.data_source_template_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_template_ids, 'DataSourceTemplateIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.data_source_template_ids_shrink):
            body['DataSourceTemplateIds'] = request.data_source_template_ids_shrink
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSourceTemplates',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataSourceTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_templates(
        self,
        request: cloud_siem_20241212_models.ListDataSourceTemplatesRequest,
    ) -> cloud_siem_20241212_models.ListDataSourceTemplatesResponse:
        """
        @summary 查询数据源模板
        
        @param request: ListDataSourceTemplatesRequest
        @return: ListDataSourceTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_templates_with_options(request, runtime)

    async def list_data_source_templates_async(
        self,
        request: cloud_siem_20241212_models.ListDataSourceTemplatesRequest,
    ) -> cloud_siem_20241212_models.ListDataSourceTemplatesResponse:
        """
        @summary 查询数据源模板
        
        @param request: ListDataSourceTemplatesRequest
        @return: ListDataSourceTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_templates_with_options_async(request, runtime)

    def list_data_sources_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataSourcesResponse:
        """
        @summary 获取厂商列表
        
        @param tmp_req: ListDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'simple')
        if not UtilClient.is_unset(tmp_req.data_source_template_ids):
            request.data_source_template_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_template_ids, 'DataSourceTemplateIds', 'simple')
        if not UtilClient.is_unset(tmp_req.log_user_ids):
            request.log_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_status):
            body['DataSourceStatus'] = request.data_source_status
        if not UtilClient.is_unset(request.data_source_store_status):
            body['DataSourceStoreStatus'] = request.data_source_store_status
        if not UtilClient.is_unset(request.data_source_template_ids_shrink):
            body['DataSourceTemplateIds'] = request.data_source_template_ids_shrink
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDataSourcesResponse:
        """
        @summary 获取厂商列表
        
        @param tmp_req: ListDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'simple')
        if not UtilClient.is_unset(tmp_req.data_source_template_ids):
            request.data_source_template_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_template_ids, 'DataSourceTemplateIds', 'simple')
        if not UtilClient.is_unset(tmp_req.log_user_ids):
            request.log_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_status):
            body['DataSourceStatus'] = request.data_source_status
        if not UtilClient.is_unset(request.data_source_store_status):
            body['DataSourceStoreStatus'] = request.data_source_store_status
        if not UtilClient.is_unset(request.data_source_template_ids_shrink):
            body['DataSourceTemplateIds'] = request.data_source_template_ids_shrink
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        request: cloud_siem_20241212_models.ListDataSourcesRequest,
    ) -> cloud_siem_20241212_models.ListDataSourcesResponse:
        """
        @summary 获取厂商列表
        
        @param request: ListDataSourcesRequest
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    async def list_data_sources_async(
        self,
        request: cloud_siem_20241212_models.ListDataSourcesRequest,
    ) -> cloud_siem_20241212_models.ListDataSourcesResponse:
        """
        @summary 获取厂商列表
        
        @param request: ListDataSourcesRequest
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_sources_with_options_async(request, runtime)

    def list_detection_rules_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListDetectionRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDetectionRulesResponse:
        """
        @summary 获取检测规则列表
        
        @param tmp_req: ListDetectionRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDetectionRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDetectionRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detection_rule_ids):
            request.detection_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detection_rule_ids, 'DetectionRuleIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not UtilClient.is_unset(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not UtilClient.is_unset(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not UtilClient.is_unset(request.detection_rule_ids_shrink):
            body['DetectionRuleIds'] = request.detection_rule_ids_shrink
        if not UtilClient.is_unset(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not UtilClient.is_unset(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not UtilClient.is_unset(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not UtilClient.is_unset(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not UtilClient.is_unset(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDetectionRules',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDetectionRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_detection_rules_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListDetectionRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListDetectionRulesResponse:
        """
        @summary 获取检测规则列表
        
        @param tmp_req: ListDetectionRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDetectionRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListDetectionRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detection_rule_ids):
            request.detection_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detection_rule_ids, 'DetectionRuleIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not UtilClient.is_unset(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not UtilClient.is_unset(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not UtilClient.is_unset(request.detection_rule_ids_shrink):
            body['DetectionRuleIds'] = request.detection_rule_ids_shrink
        if not UtilClient.is_unset(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not UtilClient.is_unset(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not UtilClient.is_unset(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not UtilClient.is_unset(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not UtilClient.is_unset(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDetectionRules',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListDetectionRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_detection_rules(
        self,
        request: cloud_siem_20241212_models.ListDetectionRulesRequest,
    ) -> cloud_siem_20241212_models.ListDetectionRulesResponse:
        """
        @summary 获取检测规则列表
        
        @param request: ListDetectionRulesRequest
        @return: ListDetectionRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_detection_rules_with_options(request, runtime)

    async def list_detection_rules_async(
        self,
        request: cloud_siem_20241212_models.ListDetectionRulesRequest,
    ) -> cloud_siem_20241212_models.ListDetectionRulesResponse:
        """
        @summary 获取检测规则列表
        
        @param request: ListDetectionRulesRequest
        @return: ListDetectionRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_detection_rules_with_options_async(request, runtime)

    def list_incidents_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListIncidentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListIncidentsResponse:
        """
        @summary 获取事件列表
        
        @param tmp_req: ListIncidentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIncidentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListIncidentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.incident_uuids):
            request.incident_uuids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.incident_uuids, 'IncidentUuids', 'simple')
        query = {}
        if not UtilClient.is_unset(request.incident_name):
            query['IncidentName'] = request.incident_name
        if not UtilClient.is_unset(request.incident_uuids_shrink):
            query['IncidentUuids'] = request.incident_uuids_shrink
        body = {}
        if not UtilClient.is_unset(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.incident_status):
            body['IncidentStatus'] = request.incident_status
        if not UtilClient.is_unset(request.incident_tags):
            body['IncidentTags'] = request.incident_tags
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relate_asset_id):
            body['RelateAssetId'] = request.relate_asset_id
        if not UtilClient.is_unset(request.relate_entity_id):
            body['RelateEntityId'] = request.relate_entity_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidents',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListIncidentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_incidents_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListIncidentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListIncidentsResponse:
        """
        @summary 获取事件列表
        
        @param tmp_req: ListIncidentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIncidentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListIncidentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.incident_uuids):
            request.incident_uuids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.incident_uuids, 'IncidentUuids', 'simple')
        query = {}
        if not UtilClient.is_unset(request.incident_name):
            query['IncidentName'] = request.incident_name
        if not UtilClient.is_unset(request.incident_uuids_shrink):
            query['IncidentUuids'] = request.incident_uuids_shrink
        body = {}
        if not UtilClient.is_unset(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.incident_status):
            body['IncidentStatus'] = request.incident_status
        if not UtilClient.is_unset(request.incident_tags):
            body['IncidentTags'] = request.incident_tags
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relate_asset_id):
            body['RelateAssetId'] = request.relate_asset_id
        if not UtilClient.is_unset(request.relate_entity_id):
            body['RelateEntityId'] = request.relate_entity_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            body['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidents',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListIncidentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_incidents(
        self,
        request: cloud_siem_20241212_models.ListIncidentsRequest,
    ) -> cloud_siem_20241212_models.ListIncidentsResponse:
        """
        @summary 获取事件列表
        
        @param request: ListIncidentsRequest
        @return: ListIncidentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_incidents_with_options(request, runtime)

    async def list_incidents_async(
        self,
        request: cloud_siem_20241212_models.ListIncidentsRequest,
    ) -> cloud_siem_20241212_models.ListIncidentsResponse:
        """
        @summary 获取事件列表
        
        @param request: ListIncidentsRequest
        @return: ListIncidentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_incidents_with_options_async(request, runtime)

    def list_log_projects_with_options(
        self,
        request: cloud_siem_20241212_models.ListLogProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListLogProjectsResponse:
        """
        @summary 获取日志Project列表
        
        @param request: ListLogProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogProjectsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLogProjects',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListLogProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_projects_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListLogProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListLogProjectsResponse:
        """
        @summary 获取日志Project列表
        
        @param request: ListLogProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogProjectsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLogProjects',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListLogProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_projects(
        self,
        request: cloud_siem_20241212_models.ListLogProjectsRequest,
    ) -> cloud_siem_20241212_models.ListLogProjectsResponse:
        """
        @summary 获取日志Project列表
        
        @param request: ListLogProjectsRequest
        @return: ListLogProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_log_projects_with_options(request, runtime)

    async def list_log_projects_async(
        self,
        request: cloud_siem_20241212_models.ListLogProjectsRequest,
    ) -> cloud_siem_20241212_models.ListLogProjectsResponse:
        """
        @summary 获取日志Project列表
        
        @param request: ListLogProjectsRequest
        @return: ListLogProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_log_projects_with_options_async(request, runtime)

    def list_log_regions_with_options(
        self,
        request: cloud_siem_20241212_models.ListLogRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListLogRegionsResponse:
        """
        @summary 获取所有的区域
        
        @param request: ListLogRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLogRegions',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListLogRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_regions_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListLogRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListLogRegionsResponse:
        """
        @summary 获取所有的区域
        
        @param request: ListLogRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLogRegions',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListLogRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_regions(
        self,
        request: cloud_siem_20241212_models.ListLogRegionsRequest,
    ) -> cloud_siem_20241212_models.ListLogRegionsResponse:
        """
        @summary 获取所有的区域
        
        @param request: ListLogRegionsRequest
        @return: ListLogRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_log_regions_with_options(request, runtime)

    async def list_log_regions_async(
        self,
        request: cloud_siem_20241212_models.ListLogRegionsRequest,
    ) -> cloud_siem_20241212_models.ListLogRegionsResponse:
        """
        @summary 获取所有的区域
        
        @param request: ListLogRegionsRequest
        @return: ListLogRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_log_regions_with_options_async(request, runtime)

    def list_log_stores_with_options(
        self,
        request: cloud_siem_20241212_models.ListLogStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListLogStoresResponse:
        """
        @summary 获取日志store列表
        
        @param request: ListLogStoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogStoresResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListLogStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_stores_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListLogStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListLogStoresResponse:
        """
        @summary 获取日志store列表
        
        @param request: ListLogStoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogStoresResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListLogStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_stores(
        self,
        request: cloud_siem_20241212_models.ListLogStoresRequest,
    ) -> cloud_siem_20241212_models.ListLogStoresResponse:
        """
        @summary 获取日志store列表
        
        @param request: ListLogStoresRequest
        @return: ListLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_log_stores_with_options(request, runtime)

    async def list_log_stores_async(
        self,
        request: cloud_siem_20241212_models.ListLogStoresRequest,
    ) -> cloud_siem_20241212_models.ListLogStoresResponse:
        """
        @summary 获取日志store列表
        
        @param request: ListLogStoresRequest
        @return: ListLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_log_stores_with_options_async(request, runtime)

    def list_normalization_categories_with_options(
        self,
        request: cloud_siem_20241212_models.ListNormalizationCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationCategoriesResponse:
        """
        @summary 获取标准化目录
        
        @param request: ListNormalizationCategoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationCategoriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_category_type):
            body['NormalizationCategoryType'] = request.normalization_category_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationCategories',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_categories_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationCategoriesResponse:
        """
        @summary 获取标准化目录
        
        @param request: ListNormalizationCategoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationCategoriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_category_type):
            body['NormalizationCategoryType'] = request.normalization_category_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationCategories',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_categories(
        self,
        request: cloud_siem_20241212_models.ListNormalizationCategoriesRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationCategoriesResponse:
        """
        @summary 获取标准化目录
        
        @param request: ListNormalizationCategoriesRequest
        @return: ListNormalizationCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_normalization_categories_with_options(request, runtime)

    async def list_normalization_categories_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationCategoriesRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationCategoriesResponse:
        """
        @summary 获取标准化目录
        
        @param request: ListNormalizationCategoriesRequest
        @return: ListNormalizationCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_normalization_categories_with_options_async(request, runtime)

    def list_normalization_fields_with_options(
        self,
        request: cloud_siem_20241212_models.ListNormalizationFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationFieldsResponse:
        """
        @summary 获取标准化日志所有字段
        
        @param request: ListNormalizationFieldsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationFieldsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationFields',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_fields_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationFieldsResponse:
        """
        @summary 获取标准化日志所有字段
        
        @param request: ListNormalizationFieldsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationFieldsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationFields',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_fields(
        self,
        request: cloud_siem_20241212_models.ListNormalizationFieldsRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationFieldsResponse:
        """
        @summary 获取标准化日志所有字段
        
        @param request: ListNormalizationFieldsRequest
        @return: ListNormalizationFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_normalization_fields_with_options(request, runtime)

    async def list_normalization_fields_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationFieldsRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationFieldsResponse:
        """
        @summary 获取标准化日志所有字段
        
        @param request: ListNormalizationFieldsRequest
        @return: ListNormalizationFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_normalization_fields_with_options_async(request, runtime)

    def list_normalization_rule_capacities_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListNormalizationRuleCapacitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationRuleCapacitiesResponse:
        """
        @summary 获取规则的安全能力
        
        @param tmp_req: ListNormalizationRuleCapacitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationRuleCapacitiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListNormalizationRuleCapacitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationRuleCapacities',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationRuleCapacitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_rule_capacities_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListNormalizationRuleCapacitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationRuleCapacitiesResponse:
        """
        @summary 获取规则的安全能力
        
        @param tmp_req: ListNormalizationRuleCapacitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationRuleCapacitiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListNormalizationRuleCapacitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationRuleCapacities',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationRuleCapacitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_rule_capacities(
        self,
        request: cloud_siem_20241212_models.ListNormalizationRuleCapacitiesRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationRuleCapacitiesResponse:
        """
        @summary 获取规则的安全能力
        
        @param request: ListNormalizationRuleCapacitiesRequest
        @return: ListNormalizationRuleCapacitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_normalization_rule_capacities_with_options(request, runtime)

    async def list_normalization_rule_capacities_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationRuleCapacitiesRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationRuleCapacitiesResponse:
        """
        @summary 获取规则的安全能力
        
        @param request: ListNormalizationRuleCapacitiesRequest
        @return: ListNormalizationRuleCapacitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_normalization_rule_capacities_with_options_async(request, runtime)

    def list_normalization_rule_versions_with_options(
        self,
        request: cloud_siem_20241212_models.ListNormalizationRuleVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationRuleVersionsResponse:
        """
        @summary 获取标准化规则版本列表
        
        @param request: ListNormalizationRuleVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationRuleVersionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationRuleVersions',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationRuleVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_rule_versions_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationRuleVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationRuleVersionsResponse:
        """
        @summary 获取标准化规则版本列表
        
        @param request: ListNormalizationRuleVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationRuleVersionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationRuleVersions',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationRuleVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_rule_versions(
        self,
        request: cloud_siem_20241212_models.ListNormalizationRuleVersionsRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationRuleVersionsResponse:
        """
        @summary 获取标准化规则版本列表
        
        @param request: ListNormalizationRuleVersionsRequest
        @return: ListNormalizationRuleVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_normalization_rule_versions_with_options(request, runtime)

    async def list_normalization_rule_versions_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationRuleVersionsRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationRuleVersionsResponse:
        """
        @summary 获取标准化规则版本列表
        
        @param request: ListNormalizationRuleVersionsRequest
        @return: ListNormalizationRuleVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_normalization_rule_versions_with_options_async(request, runtime)

    def list_normalization_rules_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListNormalizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationRulesResponse:
        """
        @summary 获取标准化规则列表
        
        @param tmp_req: ListNormalizationRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListNormalizationRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not UtilClient.is_unset(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not UtilClient.is_unset(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not UtilClient.is_unset(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationRules',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_rules_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListNormalizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationRulesResponse:
        """
        @summary 获取标准化规则列表
        
        @param tmp_req: ListNormalizationRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListNormalizationRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not UtilClient.is_unset(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not UtilClient.is_unset(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not UtilClient.is_unset(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationRules',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_rules(
        self,
        request: cloud_siem_20241212_models.ListNormalizationRulesRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationRulesResponse:
        """
        @summary 获取标准化规则列表
        
        @param request: ListNormalizationRulesRequest
        @return: ListNormalizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_normalization_rules_with_options(request, runtime)

    async def list_normalization_rules_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationRulesRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationRulesResponse:
        """
        @summary 获取标准化规则列表
        
        @param request: ListNormalizationRulesRequest
        @return: ListNormalizationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_normalization_rules_with_options_async(request, runtime)

    def list_normalization_schemas_with_options(
        self,
        request: cloud_siem_20241212_models.ListNormalizationSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationSchemasResponse:
        """
        @summary 获取标准化类目
        
        @param request: ListNormalizationSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationSchemasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not UtilClient.is_unset(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationSchemas',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_schemas_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListNormalizationSchemasResponse:
        """
        @summary 获取标准化类目
        
        @param request: ListNormalizationSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNormalizationSchemasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not UtilClient.is_unset(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNormalizationSchemas',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListNormalizationSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_schemas(
        self,
        request: cloud_siem_20241212_models.ListNormalizationSchemasRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationSchemasResponse:
        """
        @summary 获取标准化类目
        
        @param request: ListNormalizationSchemasRequest
        @return: ListNormalizationSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_normalization_schemas_with_options(request, runtime)

    async def list_normalization_schemas_async(
        self,
        request: cloud_siem_20241212_models.ListNormalizationSchemasRequest,
    ) -> cloud_siem_20241212_models.ListNormalizationSchemasResponse:
        """
        @summary 获取标准化类目
        
        @param request: ListNormalizationSchemasRequest
        @return: ListNormalizationSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_normalization_schemas_with_options_async(request, runtime)

    def list_products_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListProductsResponse:
        """
        @summary 获取产品列表
        
        @param tmp_req: ListProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListProductsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_ids):
            request.product_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_ids, 'ProductIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_ids_shrink):
            body['ProductIds'] = request.product_ids_shrink
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListProductsResponse:
        """
        @summary 获取产品列表
        
        @param tmp_req: ListProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListProductsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_ids):
            request.product_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_ids, 'ProductIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_ids_shrink):
            body['ProductIds'] = request.product_ids_shrink
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: cloud_siem_20241212_models.ListProductsRequest,
    ) -> cloud_siem_20241212_models.ListProductsResponse:
        """
        @summary 获取产品列表
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: cloud_siem_20241212_models.ListProductsRequest,
    ) -> cloud_siem_20241212_models.ListProductsResponse:
        """
        @summary 获取产品列表
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def list_traffic_statistics_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListTrafficStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListTrafficStatisticsResponse:
        """
        @summary 获取接入流量统计
        
        @param tmp_req: ListTrafficStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrafficStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListTrafficStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.log_user_ids):
            request.log_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_tag):
            body['RegionTag'] = request.region_tag
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.traffic_statistic_period):
            body['TrafficStatisticPeriod'] = request.traffic_statistic_period
        if not UtilClient.is_unset(request.traffic_statistic_period_type):
            body['TrafficStatisticPeriodType'] = request.traffic_statistic_period_type
        if not UtilClient.is_unset(request.traffic_statistic_type):
            body['TrafficStatisticType'] = request.traffic_statistic_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrafficStatistics',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListTrafficStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traffic_statistics_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListTrafficStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListTrafficStatisticsResponse:
        """
        @summary 获取接入流量统计
        
        @param tmp_req: ListTrafficStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrafficStatisticsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListTrafficStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.log_user_ids):
            request.log_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_tag):
            body['RegionTag'] = request.region_tag
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.traffic_statistic_period):
            body['TrafficStatisticPeriod'] = request.traffic_statistic_period
        if not UtilClient.is_unset(request.traffic_statistic_period_type):
            body['TrafficStatisticPeriodType'] = request.traffic_statistic_period_type
        if not UtilClient.is_unset(request.traffic_statistic_type):
            body['TrafficStatisticType'] = request.traffic_statistic_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrafficStatistics',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListTrafficStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traffic_statistics(
        self,
        request: cloud_siem_20241212_models.ListTrafficStatisticsRequest,
    ) -> cloud_siem_20241212_models.ListTrafficStatisticsResponse:
        """
        @summary 获取接入流量统计
        
        @param request: ListTrafficStatisticsRequest
        @return: ListTrafficStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_traffic_statistics_with_options(request, runtime)

    async def list_traffic_statistics_async(
        self,
        request: cloud_siem_20241212_models.ListTrafficStatisticsRequest,
    ) -> cloud_siem_20241212_models.ListTrafficStatisticsResponse:
        """
        @summary 获取接入流量统计
        
        @param request: ListTrafficStatisticsRequest
        @return: ListTrafficStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_traffic_statistics_with_options_async(request, runtime)

    def list_upgrade_items_with_options(
        self,
        request: cloud_siem_20241212_models.ListUpgradeItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListUpgradeItemsResponse:
        """
        @summary 获取升级项列表
        
        @param request: ListUpgradeItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUpgradeItemsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUpgradeItems',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListUpgradeItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upgrade_items_with_options_async(
        self,
        request: cloud_siem_20241212_models.ListUpgradeItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListUpgradeItemsResponse:
        """
        @summary 获取升级项列表
        
        @param request: ListUpgradeItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUpgradeItemsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUpgradeItems',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListUpgradeItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upgrade_items(
        self,
        request: cloud_siem_20241212_models.ListUpgradeItemsRequest,
    ) -> cloud_siem_20241212_models.ListUpgradeItemsResponse:
        """
        @summary 获取升级项列表
        
        @param request: ListUpgradeItemsRequest
        @return: ListUpgradeItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_upgrade_items_with_options(request, runtime)

    async def list_upgrade_items_async(
        self,
        request: cloud_siem_20241212_models.ListUpgradeItemsRequest,
    ) -> cloud_siem_20241212_models.ListUpgradeItemsResponse:
        """
        @summary 获取升级项列表
        
        @param request: ListUpgradeItemsRequest
        @return: ListUpgradeItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_upgrade_items_with_options_async(request, runtime)

    def list_vendors_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.ListVendorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListVendorsResponse:
        """
        @summary 获取厂商列表
        
        @param tmp_req: ListVendorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVendorsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListVendorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vendor_ids):
            request.vendor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vendor_ids, 'VendorIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_ids_shrink):
            body['VendorIds'] = request.vendor_ids_shrink
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        if not UtilClient.is_unset(request.vendor_type):
            body['VendorType'] = request.vendor_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVendors',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListVendorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vendors_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.ListVendorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ListVendorsResponse:
        """
        @summary 获取厂商列表
        
        @param tmp_req: ListVendorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVendorsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.ListVendorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vendor_ids):
            request.vendor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vendor_ids, 'VendorIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_ids_shrink):
            body['VendorIds'] = request.vendor_ids_shrink
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        if not UtilClient.is_unset(request.vendor_type):
            body['VendorType'] = request.vendor_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVendors',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ListVendorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vendors(
        self,
        request: cloud_siem_20241212_models.ListVendorsRequest,
    ) -> cloud_siem_20241212_models.ListVendorsResponse:
        """
        @summary 获取厂商列表
        
        @param request: ListVendorsRequest
        @return: ListVendorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vendors_with_options(request, runtime)

    async def list_vendors_async(
        self,
        request: cloud_siem_20241212_models.ListVendorsRequest,
    ) -> cloud_siem_20241212_models.ListVendorsResponse:
        """
        @summary 获取厂商列表
        
        @param request: ListVendorsRequest
        @return: ListVendorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vendors_with_options_async(request, runtime)

    def reset_data_storage_with_options(
        self,
        request: cloud_siem_20241212_models.ResetDataStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ResetDataStorageResponse:
        """
        @summary 数据存储的清空操作，该动作会删除已有的数据，重新初始化物理存储。
        
        @param request: ResetDataStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDataStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetDataStorage',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ResetDataStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_data_storage_with_options_async(
        self,
        request: cloud_siem_20241212_models.ResetDataStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ResetDataStorageResponse:
        """
        @summary 数据存储的清空操作，该动作会删除已有的数据，重新初始化物理存储。
        
        @param request: ResetDataStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDataStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetDataStorage',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ResetDataStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_data_storage(
        self,
        request: cloud_siem_20241212_models.ResetDataStorageRequest,
    ) -> cloud_siem_20241212_models.ResetDataStorageResponse:
        """
        @summary 数据存储的清空操作，该动作会删除已有的数据，重新初始化物理存储。
        
        @param request: ResetDataStorageRequest
        @return: ResetDataStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_data_storage_with_options(request, runtime)

    async def reset_data_storage_async(
        self,
        request: cloud_siem_20241212_models.ResetDataStorageRequest,
    ) -> cloud_siem_20241212_models.ResetDataStorageResponse:
        """
        @summary 数据存储的清空操作，该动作会删除已有的数据，重新初始化物理存储。
        
        @param request: ResetDataStorageRequest
        @return: ResetDataStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_data_storage_with_options_async(request, runtime)

    def set_default_normalization_rule_version_with_options(
        self,
        request: cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionResponse:
        """
        @summary 设置标准化规则默认版本
        
        @param request: SetDefaultNormalizationRuleVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultNormalizationRuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDefaultNormalizationRuleVersion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_normalization_rule_version_with_options_async(
        self,
        request: cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionResponse:
        """
        @summary 设置标准化规则默认版本
        
        @param request: SetDefaultNormalizationRuleVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultNormalizationRuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDefaultNormalizationRuleVersion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_normalization_rule_version(
        self,
        request: cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionRequest,
    ) -> cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionResponse:
        """
        @summary 设置标准化规则默认版本
        
        @param request: SetDefaultNormalizationRuleVersionRequest
        @return: SetDefaultNormalizationRuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_default_normalization_rule_version_with_options(request, runtime)

    async def set_default_normalization_rule_version_async(
        self,
        request: cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionRequest,
    ) -> cloud_siem_20241212_models.SetDefaultNormalizationRuleVersionResponse:
        """
        @summary 设置标准化规则默认版本
        
        @param request: SetDefaultNormalizationRuleVersionRequest
        @return: SetDefaultNormalizationRuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_default_normalization_rule_version_with_options_async(request, runtime)

    def update_data_batch_ingestion_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.UpdateDataBatchIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataBatchIngestionResponse:
        """
        @summary 更新数据批量接入
        
        @param tmp_req: UpdateDataBatchIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataBatchIngestionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.UpdateDataBatchIngestionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_ingestion_ids):
            request.data_ingestion_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ingestion_ids, 'DataIngestionIds', 'simple')
        if not UtilClient.is_unset(tmp_req.log_user_ids):
            request.log_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.auto_scan_new):
            body['AutoScanNew'] = request.auto_scan_new
        if not UtilClient.is_unset(request.data_batch_ingestion_mode):
            body['DataBatchIngestionMode'] = request.data_batch_ingestion_mode
        if not UtilClient.is_unset(request.data_ingestion_ids_shrink):
            body['DataIngestionIds'] = request.data_ingestion_ids_shrink
        if not UtilClient.is_unset(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataBatchIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataBatchIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_batch_ingestion_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.UpdateDataBatchIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataBatchIngestionResponse:
        """
        @summary 更新数据批量接入
        
        @param tmp_req: UpdateDataBatchIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataBatchIngestionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.UpdateDataBatchIngestionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_ingestion_ids):
            request.data_ingestion_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ingestion_ids, 'DataIngestionIds', 'simple')
        if not UtilClient.is_unset(tmp_req.log_user_ids):
            request.log_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.auto_scan_new):
            body['AutoScanNew'] = request.auto_scan_new
        if not UtilClient.is_unset(request.data_batch_ingestion_mode):
            body['DataBatchIngestionMode'] = request.data_batch_ingestion_mode
        if not UtilClient.is_unset(request.data_ingestion_ids_shrink):
            body['DataIngestionIds'] = request.data_ingestion_ids_shrink
        if not UtilClient.is_unset(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataBatchIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataBatchIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_batch_ingestion(
        self,
        request: cloud_siem_20241212_models.UpdateDataBatchIngestionRequest,
    ) -> cloud_siem_20241212_models.UpdateDataBatchIngestionResponse:
        """
        @summary 更新数据批量接入
        
        @param request: UpdateDataBatchIngestionRequest
        @return: UpdateDataBatchIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_batch_ingestion_with_options(request, runtime)

    async def update_data_batch_ingestion_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataBatchIngestionRequest,
    ) -> cloud_siem_20241212_models.UpdateDataBatchIngestionResponse:
        """
        @summary 更新数据批量接入
        
        @param request: UpdateDataBatchIngestionRequest
        @return: UpdateDataBatchIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_batch_ingestion_with_options_async(request, runtime)

    def update_data_ingestion_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataIngestionResponse:
        """
        @summary 更新数据接入信息
        
        @param request: UpdateDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not UtilClient.is_unset(request.data_ingestion_mode):
            body['DataIngestionMode'] = request.data_ingestion_mode
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_ingestion_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataIngestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataIngestionResponse:
        """
        @summary 更新数据接入信息
        
        @param request: UpdateDataIngestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataIngestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not UtilClient.is_unset(request.data_ingestion_mode):
            body['DataIngestionMode'] = request.data_ingestion_mode
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataIngestion',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_ingestion(
        self,
        request: cloud_siem_20241212_models.UpdateDataIngestionRequest,
    ) -> cloud_siem_20241212_models.UpdateDataIngestionResponse:
        """
        @summary 更新数据接入信息
        
        @param request: UpdateDataIngestionRequest
        @return: UpdateDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_ingestion_with_options(request, runtime)

    async def update_data_ingestion_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataIngestionRequest,
    ) -> cloud_siem_20241212_models.UpdateDataIngestionResponse:
        """
        @summary 更新数据接入信息
        
        @param request: UpdateDataIngestionRequest
        @return: UpdateDataIngestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_ingestion_with_options_async(request, runtime)

    def update_data_ingestion_template_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDataIngestionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataIngestionTemplateResponse:
        """
        @summary 更新接入模板
        
        @param request: UpdateDataIngestionTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataIngestionTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_status):
            body['DataIngestionStatus'] = request.data_ingestion_status
        if not UtilClient.is_unset(request.data_ingestion_template_id):
            body['DataIngestionTemplateId'] = request.data_ingestion_template_id
        if not UtilClient.is_unset(request.data_ingestion_template_name):
            body['DataIngestionTemplateName'] = request.data_ingestion_template_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataIngestionTemplate',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataIngestionTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_ingestion_template_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataIngestionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataIngestionTemplateResponse:
        """
        @summary 更新接入模板
        
        @param request: UpdateDataIngestionTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataIngestionTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_ingestion_status):
            body['DataIngestionStatus'] = request.data_ingestion_status
        if not UtilClient.is_unset(request.data_ingestion_template_id):
            body['DataIngestionTemplateId'] = request.data_ingestion_template_id
        if not UtilClient.is_unset(request.data_ingestion_template_name):
            body['DataIngestionTemplateName'] = request.data_ingestion_template_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataIngestionTemplate',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataIngestionTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_ingestion_template(
        self,
        request: cloud_siem_20241212_models.UpdateDataIngestionTemplateRequest,
    ) -> cloud_siem_20241212_models.UpdateDataIngestionTemplateResponse:
        """
        @summary 更新接入模板
        
        @param request: UpdateDataIngestionTemplateRequest
        @return: UpdateDataIngestionTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_ingestion_template_with_options(request, runtime)

    async def update_data_ingestion_template_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataIngestionTemplateRequest,
    ) -> cloud_siem_20241212_models.UpdateDataIngestionTemplateResponse:
        """
        @summary 更新接入模板
        
        @param request: UpdateDataIngestionTemplateRequest
        @return: UpdateDataIngestionTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_ingestion_template_with_options_async(request, runtime)

    def update_data_set_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataSetResponse:
        """
        @summary 更新数据集
        
        @param request: UpdateDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_description):
            body['DataSetDescription'] = request.data_set_description
        if not UtilClient.is_unset(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not UtilClient.is_unset(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        body_flat = {}
        if not UtilClient.is_unset(request.ip_whitelist_recognizers):
            body_flat['IpWhitelistRecognizers'] = request.ip_whitelist_recognizers
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSet',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_set_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataSetResponse:
        """
        @summary 更新数据集
        
        @param request: UpdateDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_description):
            body['DataSetDescription'] = request.data_set_description
        if not UtilClient.is_unset(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not UtilClient.is_unset(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        body_flat = {}
        if not UtilClient.is_unset(request.ip_whitelist_recognizers):
            body_flat['IpWhitelistRecognizers'] = request.ip_whitelist_recognizers
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSet',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_set(
        self,
        request: cloud_siem_20241212_models.UpdateDataSetRequest,
    ) -> cloud_siem_20241212_models.UpdateDataSetResponse:
        """
        @summary 更新数据集
        
        @param request: UpdateDataSetRequest
        @return: UpdateDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_set_with_options(request, runtime)

    async def update_data_set_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataSetRequest,
    ) -> cloud_siem_20241212_models.UpdateDataSetResponse:
        """
        @summary 更新数据集
        
        @param request: UpdateDataSetRequest
        @return: UpdateDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_set_with_options_async(request, runtime)

    def update_data_set_record_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDataSetRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataSetRecordResponse:
        """
        @summary 更新数据集记录
        
        @param request: UpdateDataSetRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSetRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.data_set_records):
            body['DataSetRecords'] = request.data_set_records
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSetRecord',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataSetRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_set_record_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataSetRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataSetRecordResponse:
        """
        @summary 更新数据集记录
        
        @param request: UpdateDataSetRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSetRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not UtilClient.is_unset(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not UtilClient.is_unset(request.data_set_records):
            body['DataSetRecords'] = request.data_set_records
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSetRecord',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataSetRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_set_record(
        self,
        request: cloud_siem_20241212_models.UpdateDataSetRecordRequest,
    ) -> cloud_siem_20241212_models.UpdateDataSetRecordResponse:
        """
        @summary 更新数据集记录
        
        @param request: UpdateDataSetRecordRequest
        @return: UpdateDataSetRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_set_record_with_options(request, runtime)

    async def update_data_set_record_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataSetRecordRequest,
    ) -> cloud_siem_20241212_models.UpdateDataSetRecordResponse:
        """
        @summary 更新数据集记录
        
        @param request: UpdateDataSetRecordRequest
        @return: UpdateDataSetRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_set_record_with_options_async(request, runtime)

    def update_data_source_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataSourceResponse:
        """
        @summary 更新数据源
        
        @param request: UpdateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        body_flat = {}
        if not UtilClient.is_unset(request.data_source_stores):
            body_flat['DataSourceStores'] = request.data_source_stores
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataSourceResponse:
        """
        @summary 更新数据源
        
        @param request: UpdateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        body_flat = {}
        if not UtilClient.is_unset(request.data_source_stores):
            body_flat['DataSourceStores'] = request.data_source_stores
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source(
        self,
        request: cloud_siem_20241212_models.UpdateDataSourceRequest,
    ) -> cloud_siem_20241212_models.UpdateDataSourceResponse:
        """
        @summary 更新数据源
        
        @param request: UpdateDataSourceRequest
        @return: UpdateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    async def update_data_source_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataSourceRequest,
    ) -> cloud_siem_20241212_models.UpdateDataSourceResponse:
        """
        @summary 更新数据源
        
        @param request: UpdateDataSourceRequest
        @return: UpdateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_source_with_options_async(request, runtime)

    def update_data_source_template_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.UpdateDataSourceTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataSourceTemplateResponse:
        """
        @summary 修改数据源模板
        
        @param tmp_req: UpdateDataSourceTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.UpdateDataSourceTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.log_user_ids):
            request.log_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.data_source_recognize_enabled):
            query['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        body = {}
        if not UtilClient.is_unset(request.auto_scan_new):
            body['AutoScanNew'] = request.auto_scan_new
        if not UtilClient.is_unset(request.data_source_template_id):
            body['DataSourceTemplateId'] = request.data_source_template_id
        if not UtilClient.is_unset(request.data_source_template_name):
            body['DataSourceTemplateName'] = request.data_source_template_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_pattern):
            body['LogProjectPattern'] = request.log_project_pattern
        if not UtilClient.is_unset(request.log_region_ids):
            body['LogRegionIds'] = request.log_region_ids
        if not UtilClient.is_unset(request.log_store_pattern):
            body['LogStorePattern'] = request.log_store_pattern
        if not UtilClient.is_unset(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceTemplate',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataSourceTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_template_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.UpdateDataSourceTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataSourceTemplateResponse:
        """
        @summary 修改数据源模板
        
        @param tmp_req: UpdateDataSourceTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.UpdateDataSourceTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.log_user_ids):
            request.log_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.data_source_recognize_enabled):
            query['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        body = {}
        if not UtilClient.is_unset(request.auto_scan_new):
            body['AutoScanNew'] = request.auto_scan_new
        if not UtilClient.is_unset(request.data_source_template_id):
            body['DataSourceTemplateId'] = request.data_source_template_id
        if not UtilClient.is_unset(request.data_source_template_name):
            body['DataSourceTemplateName'] = request.data_source_template_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_pattern):
            body['LogProjectPattern'] = request.log_project_pattern
        if not UtilClient.is_unset(request.log_region_ids):
            body['LogRegionIds'] = request.log_region_ids
        if not UtilClient.is_unset(request.log_store_pattern):
            body['LogStorePattern'] = request.log_store_pattern
        if not UtilClient.is_unset(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceTemplate',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataSourceTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source_template(
        self,
        request: cloud_siem_20241212_models.UpdateDataSourceTemplateRequest,
    ) -> cloud_siem_20241212_models.UpdateDataSourceTemplateResponse:
        """
        @summary 修改数据源模板
        
        @param request: UpdateDataSourceTemplateRequest
        @return: UpdateDataSourceTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_template_with_options(request, runtime)

    async def update_data_source_template_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataSourceTemplateRequest,
    ) -> cloud_siem_20241212_models.UpdateDataSourceTemplateResponse:
        """
        @summary 修改数据源模板
        
        @param request: UpdateDataSourceTemplateRequest
        @return: UpdateDataSourceTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_source_template_with_options_async(request, runtime)

    def update_data_storage_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataStorageResponse:
        """
        @summary 获取日志管理页面里用户数据存储的详情。
        
        @param request: UpdateDataStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_storage_region_id):
            body['DataStorageRegionId'] = request.data_storage_region_id
        if not UtilClient.is_unset(request.delivery_status):
            body['DeliveryStatus'] = request.delivery_status
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataStorage',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_storage_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataStorageResponse:
        """
        @summary 获取日志管理页面里用户数据存储的详情。
        
        @param request: UpdateDataStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataStorageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_storage_region_id):
            body['DataStorageRegionId'] = request.data_storage_region_id
        if not UtilClient.is_unset(request.delivery_status):
            body['DeliveryStatus'] = request.delivery_status
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataStorage',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_storage(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageRequest,
    ) -> cloud_siem_20241212_models.UpdateDataStorageResponse:
        """
        @summary 获取日志管理页面里用户数据存储的详情。
        
        @param request: UpdateDataStorageRequest
        @return: UpdateDataStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_storage_with_options(request, runtime)

    async def update_data_storage_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageRequest,
    ) -> cloud_siem_20241212_models.UpdateDataStorageResponse:
        """
        @summary 获取日志管理页面里用户数据存储的详情。
        
        @param request: UpdateDataStorageRequest
        @return: UpdateDataStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_storage_with_options_async(request, runtime)

    def update_data_storage_delivery_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataStorageDeliveryResponse:
        """
        @summary 操作日志投递.
        
        @param request: UpdateDataStorageDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataStorageDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.log_delivery_status):
            body['LogDeliveryStatus'] = request.log_delivery_status
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataStorageDelivery',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataStorageDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_storage_delivery_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataStorageDeliveryResponse:
        """
        @summary 操作日志投递.
        
        @param request: UpdateDataStorageDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataStorageDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.log_delivery_status):
            body['LogDeliveryStatus'] = request.log_delivery_status
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataStorageDelivery',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataStorageDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_storage_delivery(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageDeliveryRequest,
    ) -> cloud_siem_20241212_models.UpdateDataStorageDeliveryResponse:
        """
        @summary 操作日志投递.
        
        @param request: UpdateDataStorageDeliveryRequest
        @return: UpdateDataStorageDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_storage_delivery_with_options(request, runtime)

    async def update_data_storage_delivery_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageDeliveryRequest,
    ) -> cloud_siem_20241212_models.UpdateDataStorageDeliveryResponse:
        """
        @summary 操作日志投递.
        
        @param request: UpdateDataStorageDeliveryRequest
        @return: UpdateDataStorageDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_storage_delivery_with_options_async(request, runtime)

    def update_data_storage_ttl_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataStorageTtlResponse:
        """
        @summary 更新数据存储中日志的数据保存天数。
        
        @param request: UpdateDataStorageTtlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataStorageTtlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_store_cold_ttl):
            body['LogStoreColdTtl'] = request.log_store_cold_ttl
        if not UtilClient.is_unset(request.log_store_hot_ttl):
            body['LogStoreHotTtl'] = request.log_store_hot_ttl
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_store_ttl):
            body['LogStoreTtl'] = request.log_store_ttl
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataStorageTtl',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataStorageTtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_storage_ttl_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDataStorageTtlResponse:
        """
        @summary 更新数据存储中日志的数据保存天数。
        
        @param request: UpdateDataStorageTtlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataStorageTtlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_store_cold_ttl):
            body['LogStoreColdTtl'] = request.log_store_cold_ttl
        if not UtilClient.is_unset(request.log_store_hot_ttl):
            body['LogStoreHotTtl'] = request.log_store_hot_ttl
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_store_ttl):
            body['LogStoreTtl'] = request.log_store_ttl
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataStorageTtl',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDataStorageTtlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_storage_ttl(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageTtlRequest,
    ) -> cloud_siem_20241212_models.UpdateDataStorageTtlResponse:
        """
        @summary 更新数据存储中日志的数据保存天数。
        
        @param request: UpdateDataStorageTtlRequest
        @return: UpdateDataStorageTtlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_storage_ttl_with_options(request, runtime)

    async def update_data_storage_ttl_async(
        self,
        request: cloud_siem_20241212_models.UpdateDataStorageTtlRequest,
    ) -> cloud_siem_20241212_models.UpdateDataStorageTtlResponse:
        """
        @summary 更新数据存储中日志的数据保存天数。
        
        @param request: UpdateDataStorageTtlRequest
        @return: UpdateDataStorageTtlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_storage_ttl_with_options_async(request, runtime)

    def update_detection_rule_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateDetectionRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDetectionRuleResponse:
        """
        @summary 更新检测规则
        
        @param request: UpdateDetectionRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDetectionRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not UtilClient.is_unset(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_schema_id):
            body['AlertSchemaId'] = request.alert_schema_id
        if not UtilClient.is_unset(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not UtilClient.is_unset(request.alert_threshold_count):
            body['AlertThresholdCount'] = request.alert_threshold_count
        if not UtilClient.is_unset(request.alert_threshold_group):
            body['AlertThresholdGroup'] = request.alert_threshold_group
        if not UtilClient.is_unset(request.alert_threshold_period):
            body['AlertThresholdPeriod'] = request.alert_threshold_period
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.detection_expression_content):
            body['DetectionExpressionContent'] = request.detection_expression_content
        if not UtilClient.is_unset(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not UtilClient.is_unset(request.detection_rule_description):
            body['DetectionRuleDescription'] = request.detection_rule_description
        if not UtilClient.is_unset(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not UtilClient.is_unset(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not UtilClient.is_unset(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not UtilClient.is_unset(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not UtilClient.is_unset(request.entity_mappings):
            body['EntityMappings'] = request.entity_mappings
        if not UtilClient.is_unset(request.incident_aggregation_expression):
            body['IncidentAggregationExpression'] = request.incident_aggregation_expression
        if not UtilClient.is_unset(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not UtilClient.is_unset(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not UtilClient.is_unset(request.playbook_parameters):
            body['PlaybookParameters'] = request.playbook_parameters
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schedule_begin_time):
            body['ScheduleBeginTime'] = request.schedule_begin_time
        if not UtilClient.is_unset(request.schedule_expression):
            body['ScheduleExpression'] = request.schedule_expression
        if not UtilClient.is_unset(request.schedule_max_retries):
            body['ScheduleMaxRetries'] = request.schedule_max_retries
        if not UtilClient.is_unset(request.schedule_max_timeout):
            body['ScheduleMaxTimeout'] = request.schedule_max_timeout
        if not UtilClient.is_unset(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.schedule_window):
            body['ScheduleWindow'] = request.schedule_window
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDetectionRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDetectionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_detection_rule_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateDetectionRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateDetectionRuleResponse:
        """
        @summary 更新检测规则
        
        @param request: UpdateDetectionRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDetectionRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not UtilClient.is_unset(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_schema_id):
            body['AlertSchemaId'] = request.alert_schema_id
        if not UtilClient.is_unset(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not UtilClient.is_unset(request.alert_threshold_count):
            body['AlertThresholdCount'] = request.alert_threshold_count
        if not UtilClient.is_unset(request.alert_threshold_group):
            body['AlertThresholdGroup'] = request.alert_threshold_group
        if not UtilClient.is_unset(request.alert_threshold_period):
            body['AlertThresholdPeriod'] = request.alert_threshold_period
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.detection_expression_content):
            body['DetectionExpressionContent'] = request.detection_expression_content
        if not UtilClient.is_unset(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not UtilClient.is_unset(request.detection_rule_description):
            body['DetectionRuleDescription'] = request.detection_rule_description
        if not UtilClient.is_unset(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not UtilClient.is_unset(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not UtilClient.is_unset(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not UtilClient.is_unset(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not UtilClient.is_unset(request.entity_mappings):
            body['EntityMappings'] = request.entity_mappings
        if not UtilClient.is_unset(request.incident_aggregation_expression):
            body['IncidentAggregationExpression'] = request.incident_aggregation_expression
        if not UtilClient.is_unset(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not UtilClient.is_unset(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not UtilClient.is_unset(request.playbook_parameters):
            body['PlaybookParameters'] = request.playbook_parameters
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schedule_begin_time):
            body['ScheduleBeginTime'] = request.schedule_begin_time
        if not UtilClient.is_unset(request.schedule_expression):
            body['ScheduleExpression'] = request.schedule_expression
        if not UtilClient.is_unset(request.schedule_max_retries):
            body['ScheduleMaxRetries'] = request.schedule_max_retries
        if not UtilClient.is_unset(request.schedule_max_timeout):
            body['ScheduleMaxTimeout'] = request.schedule_max_timeout
        if not UtilClient.is_unset(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.schedule_window):
            body['ScheduleWindow'] = request.schedule_window
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDetectionRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateDetectionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_detection_rule(
        self,
        request: cloud_siem_20241212_models.UpdateDetectionRuleRequest,
    ) -> cloud_siem_20241212_models.UpdateDetectionRuleResponse:
        """
        @summary 更新检测规则
        
        @param request: UpdateDetectionRuleRequest
        @return: UpdateDetectionRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_detection_rule_with_options(request, runtime)

    async def update_detection_rule_async(
        self,
        request: cloud_siem_20241212_models.UpdateDetectionRuleRequest,
    ) -> cloud_siem_20241212_models.UpdateDetectionRuleResponse:
        """
        @summary 更新检测规则
        
        @param request: UpdateDetectionRuleRequest
        @return: UpdateDetectionRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_detection_rule_with_options_async(request, runtime)

    def update_normalization_rule_with_options(
        self,
        tmp_req: cloud_siem_20241212_models.UpdateNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateNormalizationRuleResponse:
        """
        @summary 更新标准化规则
        
        @param tmp_req: UpdateNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNormalizationRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.UpdateNormalizationRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_description):
            body['NormalizationRuleDescription'] = request.normalization_rule_description
        if not UtilClient.is_unset(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not UtilClient.is_unset(request.normalization_rule_format):
            body['NormalizationRuleFormat'] = request.normalization_rule_format
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not UtilClient.is_unset(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not UtilClient.is_unset(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not UtilClient.is_unset(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_normalization_rule_with_options_async(
        self,
        tmp_req: cloud_siem_20241212_models.UpdateNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateNormalizationRuleResponse:
        """
        @summary 更新标准化规则
        
        @param tmp_req: UpdateNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNormalizationRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_siem_20241212_models.UpdateNormalizationRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_rule_description):
            body['NormalizationRuleDescription'] = request.normalization_rule_description
        if not UtilClient.is_unset(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not UtilClient.is_unset(request.normalization_rule_format):
            body['NormalizationRuleFormat'] = request.normalization_rule_format
        if not UtilClient.is_unset(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not UtilClient.is_unset(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not UtilClient.is_unset(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not UtilClient.is_unset(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not UtilClient.is_unset(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_normalization_rule(
        self,
        request: cloud_siem_20241212_models.UpdateNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.UpdateNormalizationRuleResponse:
        """
        @summary 更新标准化规则
        
        @param request: UpdateNormalizationRuleRequest
        @return: UpdateNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_normalization_rule_with_options(request, runtime)

    async def update_normalization_rule_async(
        self,
        request: cloud_siem_20241212_models.UpdateNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.UpdateNormalizationRuleResponse:
        """
        @summary 更新标准化规则
        
        @param request: UpdateNormalizationRuleRequest
        @return: UpdateNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_normalization_rule_with_options_async(request, runtime)

    def update_product_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateProductResponse:
        """
        @summary 更新产品品
        
        @param request: UpdateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateProductResponse:
        """
        @summary 更新产品品
        
        @param request: UpdateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product(
        self,
        request: cloud_siem_20241212_models.UpdateProductRequest,
    ) -> cloud_siem_20241212_models.UpdateProductResponse:
        """
        @summary 更新产品品
        
        @param request: UpdateProductRequest
        @return: UpdateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    async def update_product_async(
        self,
        request: cloud_siem_20241212_models.UpdateProductRequest,
    ) -> cloud_siem_20241212_models.UpdateProductResponse:
        """
        @summary 更新产品品
        
        @param request: UpdateProductRequest
        @return: UpdateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_product_with_options_async(request, runtime)

    def update_vendor_with_options(
        self,
        request: cloud_siem_20241212_models.UpdateVendorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateVendorResponse:
        """
        @summary 更新厂商
        
        @param request: UpdateVendorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVendorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVendor',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateVendorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vendor_with_options_async(
        self,
        request: cloud_siem_20241212_models.UpdateVendorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.UpdateVendorResponse:
        """
        @summary 更新厂商
        
        @param request: UpdateVendorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVendorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.vendor_id):
            body['VendorId'] = request.vendor_id
        if not UtilClient.is_unset(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVendor',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.UpdateVendorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vendor(
        self,
        request: cloud_siem_20241212_models.UpdateVendorRequest,
    ) -> cloud_siem_20241212_models.UpdateVendorResponse:
        """
        @summary 更新厂商
        
        @param request: UpdateVendorRequest
        @return: UpdateVendorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_vendor_with_options(request, runtime)

    async def update_vendor_async(
        self,
        request: cloud_siem_20241212_models.UpdateVendorRequest,
    ) -> cloud_siem_20241212_models.UpdateVendorResponse:
        """
        @summary 更新厂商
        
        @param request: UpdateVendorRequest
        @return: UpdateVendorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_vendor_with_options_async(request, runtime)

    def validate_log_store_with_options(
        self,
        request: cloud_siem_20241212_models.ValidateLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ValidateLogStoreResponse:
        """
        @summary 校验LogStore
        
        @param request: ValidateLogStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateLogStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateLogStore',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ValidateLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_log_store_with_options_async(
        self,
        request: cloud_siem_20241212_models.ValidateLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ValidateLogStoreResponse:
        """
        @summary 校验LogStore
        
        @param request: ValidateLogStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateLogStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not UtilClient.is_unset(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not UtilClient.is_unset(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateLogStore',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ValidateLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_log_store(
        self,
        request: cloud_siem_20241212_models.ValidateLogStoreRequest,
    ) -> cloud_siem_20241212_models.ValidateLogStoreResponse:
        """
        @summary 校验LogStore
        
        @param request: ValidateLogStoreRequest
        @return: ValidateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_log_store_with_options(request, runtime)

    async def validate_log_store_async(
        self,
        request: cloud_siem_20241212_models.ValidateLogStoreRequest,
    ) -> cloud_siem_20241212_models.ValidateLogStoreResponse:
        """
        @summary 校验LogStore
        
        @param request: ValidateLogStoreRequest
        @return: ValidateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_log_store_with_options_async(request, runtime)

    def validate_normalization_rule_with_options(
        self,
        request: cloud_siem_20241212_models.ValidateNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ValidateNormalizationRuleResponse:
        """
        @summary 校验规则和数据
        
        @param request: ValidateNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateNormalizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ValidateNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_normalization_rule_with_options_async(
        self,
        request: cloud_siem_20241212_models.ValidateNormalizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20241212_models.ValidateNormalizationRuleResponse:
        """
        @summary 校验规则和数据
        
        @param request: ValidateNormalizationRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateNormalizationRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not UtilClient.is_unset(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateNormalizationRule',
            version='2024-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20241212_models.ValidateNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_normalization_rule(
        self,
        request: cloud_siem_20241212_models.ValidateNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.ValidateNormalizationRuleResponse:
        """
        @summary 校验规则和数据
        
        @param request: ValidateNormalizationRuleRequest
        @return: ValidateNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_normalization_rule_with_options(request, runtime)

    async def validate_normalization_rule_async(
        self,
        request: cloud_siem_20241212_models.ValidateNormalizationRuleRequest,
    ) -> cloud_siem_20241212_models.ValidateNormalizationRuleResponse:
        """
        @summary 校验规则和数据
        
        @param request: ValidateNormalizationRuleRequest
        @return: ValidateNormalizationRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_normalization_rule_with_options_async(request, runtime)
