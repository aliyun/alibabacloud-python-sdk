# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sddp20260120 import models as main_models
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

    def check_data_masking_instance_with_options(
        self,
        request: main_models.CheckDataMaskingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataMaskingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataMaskingInstance',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataMaskingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_masking_instance_with_options_async(
        self,
        request: main_models.CheckDataMaskingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataMaskingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataMaskingInstance',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataMaskingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_masking_instance(
        self,
        request: main_models.CheckDataMaskingInstanceRequest,
    ) -> main_models.CheckDataMaskingInstanceResponse:
        runtime = RuntimeOptions()
        return self.check_data_masking_instance_with_options(request, runtime)

    async def check_data_masking_instance_async(
        self,
        request: main_models.CheckDataMaskingInstanceRequest,
    ) -> main_models.CheckDataMaskingInstanceResponse:
        runtime = RuntimeOptions()
        return await self.check_data_masking_instance_with_options_async(request, runtime)

    def create_data_masking_rule_with_options(
        self,
        tmp_req: main_models.CreateDataMaskingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataMaskingRuleResponse:
        tmp_req.validate()
        request = main_models.CreateDataMaskingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sub_rule_list):
            request.sub_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_rule_list, 'SubRuleList', 'json')
        if not DaraCore.is_null(tmp_req.user_list):
            request.user_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        query = {}
        if not DaraCore.is_null(request.enc_algorithm):
            query['EncAlgorithm'] = request.enc_algorithm
        if not DaraCore.is_null(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not DaraCore.is_null(request.encryption_key_mode):
            query['EncryptionKeyMode'] = request.encryption_key_mode
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.expire_time_operation):
            query['ExpireTimeOperation'] = request.expire_time_operation
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_handle_id):
            query['RiskHandleId'] = request.risk_handle_id
        if not DaraCore.is_null(request.sub_rule_list_shrink):
            query['SubRuleList'] = request.sub_rule_list_shrink
        if not DaraCore.is_null(request.user_list_shrink):
            query['UserList'] = request.user_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataMaskingRule',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataMaskingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_masking_rule_with_options_async(
        self,
        tmp_req: main_models.CreateDataMaskingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataMaskingRuleResponse:
        tmp_req.validate()
        request = main_models.CreateDataMaskingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sub_rule_list):
            request.sub_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_rule_list, 'SubRuleList', 'json')
        if not DaraCore.is_null(tmp_req.user_list):
            request.user_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        query = {}
        if not DaraCore.is_null(request.enc_algorithm):
            query['EncAlgorithm'] = request.enc_algorithm
        if not DaraCore.is_null(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not DaraCore.is_null(request.encryption_key_mode):
            query['EncryptionKeyMode'] = request.encryption_key_mode
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.expire_time_operation):
            query['ExpireTimeOperation'] = request.expire_time_operation
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_handle_id):
            query['RiskHandleId'] = request.risk_handle_id
        if not DaraCore.is_null(request.sub_rule_list_shrink):
            query['SubRuleList'] = request.sub_rule_list_shrink
        if not DaraCore.is_null(request.user_list_shrink):
            query['UserList'] = request.user_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataMaskingRule',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataMaskingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_masking_rule(
        self,
        request: main_models.CreateDataMaskingRuleRequest,
    ) -> main_models.CreateDataMaskingRuleResponse:
        runtime = RuntimeOptions()
        return self.create_data_masking_rule_with_options(request, runtime)

    async def create_data_masking_rule_async(
        self,
        request: main_models.CreateDataMaskingRuleRequest,
    ) -> main_models.CreateDataMaskingRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_data_masking_rule_with_options_async(request, runtime)

    def delete_data_masking_rule_with_options(
        self,
        tmp_req: main_models.DeleteDataMaskingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataMaskingRuleResponse:
        tmp_req.validate()
        request = main_models.DeleteDataMaskingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sub_rule_list):
            request.sub_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_rule_list, 'SubRuleList', 'json')
        query = {}
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.sub_rule_list_shrink):
            query['SubRuleList'] = request.sub_rule_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataMaskingRule',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataMaskingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_masking_rule_with_options_async(
        self,
        tmp_req: main_models.DeleteDataMaskingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataMaskingRuleResponse:
        tmp_req.validate()
        request = main_models.DeleteDataMaskingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sub_rule_list):
            request.sub_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_rule_list, 'SubRuleList', 'json')
        query = {}
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.sub_rule_list_shrink):
            query['SubRuleList'] = request.sub_rule_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataMaskingRule',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataMaskingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_masking_rule(
        self,
        request: main_models.DeleteDataMaskingRuleRequest,
    ) -> main_models.DeleteDataMaskingRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_data_masking_rule_with_options(request, runtime)

    async def delete_data_masking_rule_async(
        self,
        request: main_models.DeleteDataMaskingRuleRequest,
    ) -> main_models.DeleteDataMaskingRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_masking_rule_with_options_async(request, runtime)

    def get_data_masking_account_count_with_options(
        self,
        request: main_models.GetDataMaskingAccountCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataMaskingAccountCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataMaskingAccountCount',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataMaskingAccountCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_masking_account_count_with_options_async(
        self,
        request: main_models.GetDataMaskingAccountCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataMaskingAccountCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataMaskingAccountCount',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataMaskingAccountCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_masking_account_count(
        self,
        request: main_models.GetDataMaskingAccountCountRequest,
    ) -> main_models.GetDataMaskingAccountCountResponse:
        runtime = RuntimeOptions()
        return self.get_data_masking_account_count_with_options(request, runtime)

    async def get_data_masking_account_count_async(
        self,
        request: main_models.GetDataMaskingAccountCountRequest,
    ) -> main_models.GetDataMaskingAccountCountResponse:
        runtime = RuntimeOptions()
        return await self.get_data_masking_account_count_with_options_async(request, runtime)

    def get_data_masking_column_count_with_options(
        self,
        request: main_models.GetDataMaskingColumnCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataMaskingColumnCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataMaskingColumnCount',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataMaskingColumnCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_masking_column_count_with_options_async(
        self,
        request: main_models.GetDataMaskingColumnCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataMaskingColumnCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataMaskingColumnCount',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataMaskingColumnCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_masking_column_count(
        self,
        request: main_models.GetDataMaskingColumnCountRequest,
    ) -> main_models.GetDataMaskingColumnCountResponse:
        runtime = RuntimeOptions()
        return self.get_data_masking_column_count_with_options(request, runtime)

    async def get_data_masking_column_count_async(
        self,
        request: main_models.GetDataMaskingColumnCountRequest,
    ) -> main_models.GetDataMaskingColumnCountResponse:
        runtime = RuntimeOptions()
        return await self.get_data_masking_column_count_with_options_async(request, runtime)

    def get_instance_attribute_with_options(
        self,
        request: main_models.GetInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceAttribute',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_attribute_with_options_async(
        self,
        request: main_models.GetInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceAttribute',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_attribute(
        self,
        request: main_models.GetInstanceAttributeRequest,
    ) -> main_models.GetInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_instance_attribute_with_options(request, runtime)

    async def get_instance_attribute_async(
        self,
        request: main_models.GetInstanceAttributeRequest,
    ) -> main_models.GetInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_attribute_with_options_async(request, runtime)

    def list_columns_with_options(
        self,
        request: main_models.ListColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_asset_source_id):
            query['DataAssetSourceId'] = request.data_asset_source_id
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
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
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListColumns',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_columns_with_options_async(
        self,
        request: main_models.ListColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_asset_source_id):
            query['DataAssetSourceId'] = request.data_asset_source_id
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
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
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListColumns',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_columns(
        self,
        request: main_models.ListColumnsRequest,
    ) -> main_models.ListColumnsResponse:
        runtime = RuntimeOptions()
        return self.list_columns_with_options(request, runtime)

    async def list_columns_async(
        self,
        request: main_models.ListColumnsRequest,
    ) -> main_models.ListColumnsResponse:
        runtime = RuntimeOptions()
        return await self.list_columns_with_options_async(request, runtime)

    def list_data_asset_accounts_with_options(
        self,
        request: main_models.ListDataAssetAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAssetAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.auth_role):
            query['AuthRole'] = request.auth_role
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAssetAccounts',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAssetAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_asset_accounts_with_options_async(
        self,
        request: main_models.ListDataAssetAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAssetAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.auth_role):
            query['AuthRole'] = request.auth_role
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAssetAccounts',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAssetAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_asset_accounts(
        self,
        request: main_models.ListDataAssetAccountsRequest,
    ) -> main_models.ListDataAssetAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_data_asset_accounts_with_options(request, runtime)

    async def list_data_asset_accounts_async(
        self,
        request: main_models.ListDataAssetAccountsRequest,
    ) -> main_models.ListDataAssetAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_asset_accounts_with_options_async(request, runtime)

    def list_data_masking_columns_with_options(
        self,
        request: main_models.ListDataMaskingColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataMaskingColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.column_name):
            query['ColumnName'] = request.column_name
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
        if not DaraCore.is_null(request.masking_status):
            query['MaskingStatus'] = request.masking_status
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not DaraCore.is_null(request.risk_leve_lid):
            query['RiskLeveLId'] = request.risk_leve_lid
        if not DaraCore.is_null(request.risk_level_ids):
            query['RiskLevelIds'] = request.risk_level_ids
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_rule_ids):
            query['TemplateRuleIds'] = request.template_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataMaskingColumns',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataMaskingColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_masking_columns_with_options_async(
        self,
        request: main_models.ListDataMaskingColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataMaskingColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.column_name):
            query['ColumnName'] = request.column_name
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
        if not DaraCore.is_null(request.masking_status):
            query['MaskingStatus'] = request.masking_status
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not DaraCore.is_null(request.risk_leve_lid):
            query['RiskLeveLId'] = request.risk_leve_lid
        if not DaraCore.is_null(request.risk_level_ids):
            query['RiskLevelIds'] = request.risk_level_ids
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_rule_ids):
            query['TemplateRuleIds'] = request.template_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataMaskingColumns',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataMaskingColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_masking_columns(
        self,
        request: main_models.ListDataMaskingColumnsRequest,
    ) -> main_models.ListDataMaskingColumnsResponse:
        runtime = RuntimeOptions()
        return self.list_data_masking_columns_with_options(request, runtime)

    async def list_data_masking_columns_async(
        self,
        request: main_models.ListDataMaskingColumnsRequest,
    ) -> main_models.ListDataMaskingColumnsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_masking_columns_with_options_async(request, runtime)

    def list_data_masking_encryption_algorithms_with_options(
        self,
        request: main_models.ListDataMaskingEncryptionAlgorithmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataMaskingEncryptionAlgorithmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataMaskingEncryptionAlgorithms',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataMaskingEncryptionAlgorithmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_masking_encryption_algorithms_with_options_async(
        self,
        request: main_models.ListDataMaskingEncryptionAlgorithmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataMaskingEncryptionAlgorithmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataMaskingEncryptionAlgorithms',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataMaskingEncryptionAlgorithmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_masking_encryption_algorithms(
        self,
        request: main_models.ListDataMaskingEncryptionAlgorithmsRequest,
    ) -> main_models.ListDataMaskingEncryptionAlgorithmsResponse:
        runtime = RuntimeOptions()
        return self.list_data_masking_encryption_algorithms_with_options(request, runtime)

    async def list_data_masking_encryption_algorithms_async(
        self,
        request: main_models.ListDataMaskingEncryptionAlgorithmsRequest,
    ) -> main_models.ListDataMaskingEncryptionAlgorithmsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_masking_encryption_algorithms_with_options_async(request, runtime)

    def list_data_masking_instances_with_options(
        self,
        request: main_models.ListDataMaskingInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataMaskingInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.column_name):
            query['ColumnName'] = request.column_name
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
        if not DaraCore.is_null(request.masking_status):
            query['MaskingStatus'] = request.masking_status
        if not DaraCore.is_null(request.model_tag_id):
            query['ModelTagId'] = request.model_tag_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.risk_level_ids):
            query['RiskLevelIds'] = request.risk_level_ids
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_rule_ids):
            query['TemplateRuleIds'] = request.template_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataMaskingInstances',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataMaskingInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_masking_instances_with_options_async(
        self,
        request: main_models.ListDataMaskingInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataMaskingInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.column_name):
            query['ColumnName'] = request.column_name
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
        if not DaraCore.is_null(request.masking_status):
            query['MaskingStatus'] = request.masking_status
        if not DaraCore.is_null(request.model_tag_id):
            query['ModelTagId'] = request.model_tag_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.risk_level_ids):
            query['RiskLevelIds'] = request.risk_level_ids
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_rule_ids):
            query['TemplateRuleIds'] = request.template_rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataMaskingInstances',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataMaskingInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_masking_instances(
        self,
        request: main_models.ListDataMaskingInstancesRequest,
    ) -> main_models.ListDataMaskingInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_data_masking_instances_with_options(request, runtime)

    async def list_data_masking_instances_async(
        self,
        request: main_models.ListDataMaskingInstancesRequest,
    ) -> main_models.ListDataMaskingInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_masking_instances_with_options_async(request, runtime)

    def list_data_sources_with_options(
        self,
        request: main_models.ListDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_status):
            query['ConnectStatus'] = request.connect_status
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_asset_id):
            query['DataAssetId'] = request.data_asset_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.identify_status):
            query['IdentifyStatus'] = request.identify_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2026-01-20',
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
        request: main_models.ListDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_status):
            query['ConnectStatus'] = request.connect_status
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_asset_id):
            query['DataAssetId'] = request.data_asset_id
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.identify_status):
            query['IdentifyStatus'] = request.identify_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2026-01-20',
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

    def list_identify_models_with_options(
        self,
        request: main_models.ListIdentifyModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentifyModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.filter_audit_model):
            query['FilterAuditModel'] = request.filter_audit_model
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentifyModels',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentifyModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_identify_models_with_options_async(
        self,
        request: main_models.ListIdentifyModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentifyModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.filter_audit_model):
            query['FilterAuditModel'] = request.filter_audit_model
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentifyModels',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentifyModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_identify_models(
        self,
        request: main_models.ListIdentifyModelsRequest,
    ) -> main_models.ListIdentifyModelsResponse:
        runtime = RuntimeOptions()
        return self.list_identify_models_with_options(request, runtime)

    async def list_identify_models_async(
        self,
        request: main_models.ListIdentifyModelsRequest,
    ) -> main_models.ListIdentifyModelsResponse:
        runtime = RuntimeOptions()
        return await self.list_identify_models_with_options_async(request, runtime)

    def list_kms_keys_with_options(
        self,
        request: main_models.ListKmsKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKmsKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKmsKeys',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKmsKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kms_keys_with_options_async(
        self,
        request: main_models.ListKmsKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKmsKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKmsKeys',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKmsKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kms_keys(
        self,
        request: main_models.ListKmsKeysRequest,
    ) -> main_models.ListKmsKeysResponse:
        runtime = RuntimeOptions()
        return self.list_kms_keys_with_options(request, runtime)

    async def list_kms_keys_async(
        self,
        request: main_models.ListKmsKeysRequest,
    ) -> main_models.ListKmsKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_kms_keys_with_options_async(request, runtime)

    def list_mini_engine_versions_with_options(
        self,
        request: main_models.ListMiniEngineVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMiniEngineVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMiniEngineVersions',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMiniEngineVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mini_engine_versions_with_options_async(
        self,
        request: main_models.ListMiniEngineVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMiniEngineVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMiniEngineVersions',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMiniEngineVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mini_engine_versions(
        self,
        request: main_models.ListMiniEngineVersionsRequest,
    ) -> main_models.ListMiniEngineVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_mini_engine_versions_with_options(request, runtime)

    async def list_mini_engine_versions_async(
        self,
        request: main_models.ListMiniEngineVersionsRequest,
    ) -> main_models.ListMiniEngineVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_mini_engine_versions_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audited):
            query['Audited'] = request.audited
        if not DaraCore.is_null(request.identified):
            query['Identified'] = request.identified
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audited):
            query['Audited'] = request.audited
        if not DaraCore.is_null(request.identified):
            query['Identified'] = request.identified
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_risk_levels_with_options(
        self,
        request: main_models.ListRiskLevelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRiskLevelsResponse:
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
            action = 'ListRiskLevels',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRiskLevelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_risk_levels_with_options_async(
        self,
        request: main_models.ListRiskLevelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRiskLevelsResponse:
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
            action = 'ListRiskLevels',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRiskLevelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_risk_levels(
        self,
        request: main_models.ListRiskLevelsRequest,
    ) -> main_models.ListRiskLevelsResponse:
        runtime = RuntimeOptions()
        return self.list_risk_levels_with_options(request, runtime)

    async def list_risk_levels_async(
        self,
        request: main_models.ListRiskLevelsRequest,
    ) -> main_models.ListRiskLevelsResponse:
        runtime = RuntimeOptions()
        return await self.list_risk_levels_with_options_async(request, runtime)

    def list_tables_with_options(
        self,
        request: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_asset_source_id):
            query['DataAssetSourceId'] = request.data_asset_source_id
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
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
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        request: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_asset_source_id):
            query['DataAssetSourceId'] = request.data_asset_source_id
        if not DaraCore.is_null(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
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
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        return self.list_tables_with_options(request, runtime)

    async def list_tables_async(
        self,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        return await self.list_tables_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: main_models.ListTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
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
            action = 'ListTemplates',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: main_models.ListTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
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
            action = 'ListTemplates',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def list_total_sensitive_info_with_options(
        self,
        request: main_models.ListTotalSensitiveInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTotalSensitiveInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count_type):
            query['CountType'] = request.count_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_code_list):
            query['ProductCodeList'] = request.product_code_list
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTotalSensitiveInfo',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTotalSensitiveInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_total_sensitive_info_with_options_async(
        self,
        request: main_models.ListTotalSensitiveInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTotalSensitiveInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count_type):
            query['CountType'] = request.count_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_code_list):
            query['ProductCodeList'] = request.product_code_list
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTotalSensitiveInfo',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTotalSensitiveInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_total_sensitive_info(
        self,
        request: main_models.ListTotalSensitiveInfoRequest,
    ) -> main_models.ListTotalSensitiveInfoResponse:
        runtime = RuntimeOptions()
        return self.list_total_sensitive_info_with_options(request, runtime)

    async def list_total_sensitive_info_async(
        self,
        request: main_models.ListTotalSensitiveInfoRequest,
    ) -> main_models.ListTotalSensitiveInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_total_sensitive_info_with_options_async(request, runtime)

    def sync_data_assets_with_options(
        self,
        request: main_models.SyncDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncDataAssetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncDataAssets',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDataAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_data_assets_with_options_async(
        self,
        request: main_models.SyncDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncDataAssetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncDataAssets',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDataAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_data_assets(
        self,
        request: main_models.SyncDataAssetsRequest,
    ) -> main_models.SyncDataAssetsResponse:
        runtime = RuntimeOptions()
        return self.sync_data_assets_with_options(request, runtime)

    async def sync_data_assets_async(
        self,
        request: main_models.SyncDataAssetsRequest,
    ) -> main_models.SyncDataAssetsResponse:
        runtime = RuntimeOptions()
        return await self.sync_data_assets_with_options_async(request, runtime)

    def update_data_masking_encryption_algorithm_with_options(
        self,
        request: main_models.UpdateDataMaskingEncryptionAlgorithmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataMaskingEncryptionAlgorithmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encryption_algorithm):
            query['EncryptionAlgorithm'] = request.encryption_algorithm
        if not DaraCore.is_null(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataMaskingEncryptionAlgorithm',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataMaskingEncryptionAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_masking_encryption_algorithm_with_options_async(
        self,
        request: main_models.UpdateDataMaskingEncryptionAlgorithmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataMaskingEncryptionAlgorithmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encryption_algorithm):
            query['EncryptionAlgorithm'] = request.encryption_algorithm
        if not DaraCore.is_null(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataMaskingEncryptionAlgorithm',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataMaskingEncryptionAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_masking_encryption_algorithm(
        self,
        request: main_models.UpdateDataMaskingEncryptionAlgorithmRequest,
    ) -> main_models.UpdateDataMaskingEncryptionAlgorithmResponse:
        runtime = RuntimeOptions()
        return self.update_data_masking_encryption_algorithm_with_options(request, runtime)

    async def update_data_masking_encryption_algorithm_async(
        self,
        request: main_models.UpdateDataMaskingEncryptionAlgorithmRequest,
    ) -> main_models.UpdateDataMaskingEncryptionAlgorithmResponse:
        runtime = RuntimeOptions()
        return await self.update_data_masking_encryption_algorithm_with_options_async(request, runtime)

    def update_data_masking_users_with_options(
        self,
        tmp_req: main_models.UpdateDataMaskingUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataMaskingUsersResponse:
        tmp_req.validate()
        request = main_models.UpdateDataMaskingUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_list):
            request.user_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_role):
            query['AuthRole'] = request.auth_role
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.expire_time_operation):
            query['ExpireTimeOperation'] = request.expire_time_operation
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.user_list_shrink):
            query['UserList'] = request.user_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataMaskingUsers',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataMaskingUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_masking_users_with_options_async(
        self,
        tmp_req: main_models.UpdateDataMaskingUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataMaskingUsersResponse:
        tmp_req.validate()
        request = main_models.UpdateDataMaskingUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_list):
            request.user_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_role):
            query['AuthRole'] = request.auth_role
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.expire_time_operation):
            query['ExpireTimeOperation'] = request.expire_time_operation
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.user_list_shrink):
            query['UserList'] = request.user_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataMaskingUsers',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataMaskingUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_masking_users(
        self,
        request: main_models.UpdateDataMaskingUsersRequest,
    ) -> main_models.UpdateDataMaskingUsersResponse:
        runtime = RuntimeOptions()
        return self.update_data_masking_users_with_options(request, runtime)

    async def update_data_masking_users_async(
        self,
        request: main_models.UpdateDataMaskingUsersRequest,
    ) -> main_models.UpdateDataMaskingUsersResponse:
        runtime = RuntimeOptions()
        return await self.update_data_masking_users_with_options_async(request, runtime)

    def upgrade_kernel_version_with_options(
        self,
        request: main_models.UpgradeKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.kernel_version):
            query['KernelVersion'] = request.kernel_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.upgrade_time):
            query['UpgradeTime'] = request.upgrade_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeKernelVersion',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_kernel_version_with_options_async(
        self,
        request: main_models.UpgradeKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.kernel_version):
            query['KernelVersion'] = request.kernel_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.upgrade_time):
            query['UpgradeTime'] = request.upgrade_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeKernelVersion',
            version = '2026-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_kernel_version(
        self,
        request: main_models.UpgradeKernelVersionRequest,
    ) -> main_models.UpgradeKernelVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_kernel_version_with_options(request, runtime)

    async def upgrade_kernel_version_async(
        self,
        request: main_models.UpgradeKernelVersionRequest,
    ) -> main_models.UpgradeKernelVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_kernel_version_with_options_async(request, runtime)
