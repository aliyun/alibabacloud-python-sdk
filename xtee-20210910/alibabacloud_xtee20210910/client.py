# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_xtee20210910 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('xtee', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_sample_data_by_csv_with_options(
        self,
        request: main_models.AddSampleDataByCsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSampleDataByCsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.oss_file_name):
            query['ossFileName'] = request.oss_file_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_batch_uuid):
            query['sampleBatchUuid'] = request.sample_batch_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSampleDataByCsv',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSampleDataByCsvResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sample_data_by_csv_with_options_async(
        self,
        request: main_models.AddSampleDataByCsvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSampleDataByCsvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.oss_file_name):
            query['ossFileName'] = request.oss_file_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_batch_uuid):
            query['sampleBatchUuid'] = request.sample_batch_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSampleDataByCsv',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSampleDataByCsvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sample_data_by_csv(
        self,
        request: main_models.AddSampleDataByCsvRequest,
    ) -> main_models.AddSampleDataByCsvResponse:
        runtime = RuntimeOptions()
        return self.add_sample_data_by_csv_with_options(request, runtime)

    async def add_sample_data_by_csv_async(
        self,
        request: main_models.AddSampleDataByCsvRequest,
    ) -> main_models.AddSampleDataByCsvResponse:
        runtime = RuntimeOptions()
        return await self.add_sample_data_by_csv_with_options_async(request, runtime)

    def add_sample_data_by_text_with_options(
        self,
        request: main_models.AddSampleDataByTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSampleDataByTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_batch_uuid):
            query['sampleBatchUuid'] = request.sample_batch_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSampleDataByText',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSampleDataByTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sample_data_by_text_with_options_async(
        self,
        request: main_models.AddSampleDataByTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSampleDataByTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_batch_uuid):
            query['sampleBatchUuid'] = request.sample_batch_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSampleDataByText',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSampleDataByTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sample_data_by_text(
        self,
        request: main_models.AddSampleDataByTextRequest,
    ) -> main_models.AddSampleDataByTextResponse:
        runtime = RuntimeOptions()
        return self.add_sample_data_by_text_with_options(request, runtime)

    async def add_sample_data_by_text_async(
        self,
        request: main_models.AddSampleDataByTextRequest,
    ) -> main_models.AddSampleDataByTextResponse:
        runtime = RuntimeOptions()
        return await self.add_sample_data_by_text_with_options_async(request, runtime)

    def batch_delete_sample_data_with_options(
        self,
        request: main_models.BatchDeleteSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.uuids):
            query['uuids'] = request.uuids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteSampleData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_sample_data_with_options_async(
        self,
        request: main_models.BatchDeleteSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.uuids):
            query['uuids'] = request.uuids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteSampleData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_sample_data(
        self,
        request: main_models.BatchDeleteSampleDataRequest,
    ) -> main_models.BatchDeleteSampleDataResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_sample_data_with_options(request, runtime)

    async def batch_delete_sample_data_async(
        self,
        request: main_models.BatchDeleteSampleDataRequest,
    ) -> main_models.BatchDeleteSampleDataResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_sample_data_with_options_async(request, runtime)

    def bind_variable_with_options(
        self,
        request: main_models.BindVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not DaraCore.is_null(request.api_type):
            query['apiType'] = request.api_type
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.define_id):
            query['defineId'] = request.define_id
        if not DaraCore.is_null(request.define_ids):
            query['defineIds'] = request.define_ids
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.exception_value):
            query['exceptionValue'] = request.exception_value
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.output_field):
            query['outputField'] = request.output_field
        if not DaraCore.is_null(request.output_type):
            query['outputType'] = request.output_type
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.params_list):
            query['paramsList'] = request.params_list
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_variable_with_options_async(
        self,
        request: main_models.BindVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not DaraCore.is_null(request.api_type):
            query['apiType'] = request.api_type
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.define_id):
            query['defineId'] = request.define_id
        if not DaraCore.is_null(request.define_ids):
            query['defineIds'] = request.define_ids
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.exception_value):
            query['exceptionValue'] = request.exception_value
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.output_field):
            query['outputField'] = request.output_field
        if not DaraCore.is_null(request.output_type):
            query['outputType'] = request.output_type
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.params_list):
            query['paramsList'] = request.params_list
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_variable(
        self,
        request: main_models.BindVariableRequest,
    ) -> main_models.BindVariableResponse:
        runtime = RuntimeOptions()
        return self.bind_variable_with_options(request, runtime)

    async def bind_variable_async(
        self,
        request: main_models.BindVariableRequest,
    ) -> main_models.BindVariableResponse:
        runtime = RuntimeOptions()
        return await self.bind_variable_with_options_async(request, runtime)

    def check_copy_rule_variable_with_options(
        self,
        request: main_models.CheckCopyRuleVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCopyRuleVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_type):
            query['CreateType'] = request.create_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.source_rule_id):
            query['SourceRuleId'] = request.source_rule_id
        if not DaraCore.is_null(request.source_rule_ids):
            query['SourceRuleIds'] = request.source_rule_ids
        if not DaraCore.is_null(request.target_event_code):
            query['TargetEventCode'] = request.target_event_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCopyRuleVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCopyRuleVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_copy_rule_variable_with_options_async(
        self,
        request: main_models.CheckCopyRuleVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCopyRuleVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_type):
            query['CreateType'] = request.create_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.source_rule_id):
            query['SourceRuleId'] = request.source_rule_id
        if not DaraCore.is_null(request.source_rule_ids):
            query['SourceRuleIds'] = request.source_rule_ids
        if not DaraCore.is_null(request.target_event_code):
            query['TargetEventCode'] = request.target_event_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCopyRuleVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCopyRuleVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_copy_rule_variable(
        self,
        request: main_models.CheckCopyRuleVariableRequest,
    ) -> main_models.CheckCopyRuleVariableResponse:
        runtime = RuntimeOptions()
        return self.check_copy_rule_variable_with_options(request, runtime)

    async def check_copy_rule_variable_async(
        self,
        request: main_models.CheckCopyRuleVariableRequest,
    ) -> main_models.CheckCopyRuleVariableResponse:
        runtime = RuntimeOptions()
        return await self.check_copy_rule_variable_with_options_async(request, runtime)

    def check_cust_variable_limit_with_options(
        self,
        request: main_models.CheckCustVariableLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCustVariableLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCustVariableLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCustVariableLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cust_variable_limit_with_options_async(
        self,
        request: main_models.CheckCustVariableLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCustVariableLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCustVariableLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCustVariableLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cust_variable_limit(
        self,
        request: main_models.CheckCustVariableLimitRequest,
    ) -> main_models.CheckCustVariableLimitResponse:
        runtime = RuntimeOptions()
        return self.check_cust_variable_limit_with_options(request, runtime)

    async def check_cust_variable_limit_async(
        self,
        request: main_models.CheckCustVariableLimitRequest,
    ) -> main_models.CheckCustVariableLimitResponse:
        runtime = RuntimeOptions()
        return await self.check_cust_variable_limit_with_options_async(request, runtime)

    def check_expression_variable_limit_with_options(
        self,
        request: main_models.CheckExpressionVariableLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckExpressionVariableLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckExpressionVariableLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckExpressionVariableLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_expression_variable_limit_with_options_async(
        self,
        request: main_models.CheckExpressionVariableLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckExpressionVariableLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckExpressionVariableLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckExpressionVariableLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_expression_variable_limit(
        self,
        request: main_models.CheckExpressionVariableLimitRequest,
    ) -> main_models.CheckExpressionVariableLimitResponse:
        runtime = RuntimeOptions()
        return self.check_expression_variable_limit_with_options(request, runtime)

    async def check_expression_variable_limit_async(
        self,
        request: main_models.CheckExpressionVariableLimitRequest,
    ) -> main_models.CheckExpressionVariableLimitResponse:
        runtime = RuntimeOptions()
        return await self.check_expression_variable_limit_with_options_async(request, runtime)

    def check_field_limit_with_options(
        self,
        request: main_models.CheckFieldLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckFieldLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckFieldLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckFieldLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_field_limit_with_options_async(
        self,
        request: main_models.CheckFieldLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckFieldLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckFieldLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckFieldLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_field_limit(
        self,
        request: main_models.CheckFieldLimitRequest,
    ) -> main_models.CheckFieldLimitResponse:
        runtime = RuntimeOptions()
        return self.check_field_limit_with_options(request, runtime)

    async def check_field_limit_async(
        self,
        request: main_models.CheckFieldLimitRequest,
    ) -> main_models.CheckFieldLimitResponse:
        runtime = RuntimeOptions()
        return await self.check_field_limit_with_options_async(request, runtime)

    def check_usage_variable_with_options(
        self,
        request: main_models.CheckUsageVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUsageVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUsageVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUsageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_usage_variable_with_options_async(
        self,
        request: main_models.CheckUsageVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUsageVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUsageVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUsageVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_usage_variable(
        self,
        request: main_models.CheckUsageVariableRequest,
    ) -> main_models.CheckUsageVariableResponse:
        runtime = RuntimeOptions()
        return self.check_usage_variable_with_options(request, runtime)

    async def check_usage_variable_async(
        self,
        request: main_models.CheckUsageVariableRequest,
    ) -> main_models.CheckUsageVariableResponse:
        runtime = RuntimeOptions()
        return await self.check_usage_variable_with_options_async(request, runtime)

    def compare_copy_rule_variable_with_options(
        self,
        request: main_models.CompareCopyRuleVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareCopyRuleVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_type):
            query['CreateType'] = request.create_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.source_rule_id):
            query['SourceRuleId'] = request.source_rule_id
        if not DaraCore.is_null(request.source_rule_ids):
            query['SourceRuleIds'] = request.source_rule_ids
        if not DaraCore.is_null(request.target_event_code):
            query['TargetEventCode'] = request.target_event_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompareCopyRuleVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareCopyRuleVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_copy_rule_variable_with_options_async(
        self,
        request: main_models.CompareCopyRuleVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareCopyRuleVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_type):
            query['CreateType'] = request.create_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.source_rule_id):
            query['SourceRuleId'] = request.source_rule_id
        if not DaraCore.is_null(request.source_rule_ids):
            query['SourceRuleIds'] = request.source_rule_ids
        if not DaraCore.is_null(request.target_event_code):
            query['TargetEventCode'] = request.target_event_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompareCopyRuleVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareCopyRuleVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_copy_rule_variable(
        self,
        request: main_models.CompareCopyRuleVariableRequest,
    ) -> main_models.CompareCopyRuleVariableResponse:
        runtime = RuntimeOptions()
        return self.compare_copy_rule_variable_with_options(request, runtime)

    async def compare_copy_rule_variable_async(
        self,
        request: main_models.CompareCopyRuleVariableRequest,
    ) -> main_models.CompareCopyRuleVariableResponse:
        runtime = RuntimeOptions()
        return await self.compare_copy_rule_variable_with_options_async(request, runtime)

    def compare_rule_with_options(
        self,
        request: main_models.CompareRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.previous_rule_version_id):
            query['previousRuleVersionId'] = request.previous_rule_version_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompareRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_rule_with_options_async(
        self,
        request: main_models.CompareRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.previous_rule_version_id):
            query['previousRuleVersionId'] = request.previous_rule_version_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompareRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_rule(
        self,
        request: main_models.CompareRuleRequest,
    ) -> main_models.CompareRuleResponse:
        runtime = RuntimeOptions()
        return self.compare_rule_with_options(request, runtime)

    async def compare_rule_async(
        self,
        request: main_models.CompareRuleRequest,
    ) -> main_models.CompareRuleResponse:
        runtime = RuntimeOptions()
        return await self.compare_rule_with_options_async(request, runtime)

    def create_analysis_condition_favorite_with_options(
        self,
        request: main_models.CreateAnalysisConditionFavoriteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnalysisConditionFavoriteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnalysisConditionFavorite',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnalysisConditionFavoriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_analysis_condition_favorite_with_options_async(
        self,
        request: main_models.CreateAnalysisConditionFavoriteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnalysisConditionFavoriteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnalysisConditionFavorite',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnalysisConditionFavoriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_analysis_condition_favorite(
        self,
        request: main_models.CreateAnalysisConditionFavoriteRequest,
    ) -> main_models.CreateAnalysisConditionFavoriteResponse:
        runtime = RuntimeOptions()
        return self.create_analysis_condition_favorite_with_options(request, runtime)

    async def create_analysis_condition_favorite_async(
        self,
        request: main_models.CreateAnalysisConditionFavoriteRequest,
    ) -> main_models.CreateAnalysisConditionFavoriteResponse:
        runtime = RuntimeOptions()
        return await self.create_analysis_condition_favorite_with_options_async(request, runtime)

    def create_analysis_export_task_with_options(
        self,
        request: main_models.CreateAnalysisExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnalysisExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.columns):
            query['columns'] = request.columns
        if not DaraCore.is_null(request.conditions):
            query['conditions'] = request.conditions
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.file_format):
            query['fileFormat'] = request.file_format
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnalysisExportTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnalysisExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_analysis_export_task_with_options_async(
        self,
        request: main_models.CreateAnalysisExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnalysisExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.columns):
            query['columns'] = request.columns
        if not DaraCore.is_null(request.conditions):
            query['conditions'] = request.conditions
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.file_format):
            query['fileFormat'] = request.file_format
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnalysisExportTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnalysisExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_analysis_export_task(
        self,
        request: main_models.CreateAnalysisExportTaskRequest,
    ) -> main_models.CreateAnalysisExportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_analysis_export_task_with_options(request, runtime)

    async def create_analysis_export_task_async(
        self,
        request: main_models.CreateAnalysisExportTaskRequest,
    ) -> main_models.CreateAnalysisExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_analysis_export_task_with_options_async(request, runtime)

    def create_app_key_with_options(
        self,
        request: main_models.CreateAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppKey',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_key_with_options_async(
        self,
        request: main_models.CreateAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppKey',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_key(
        self,
        request: main_models.CreateAppKeyRequest,
    ) -> main_models.CreateAppKeyResponse:
        runtime = RuntimeOptions()
        return self.create_app_key_with_options(request, runtime)

    async def create_app_key_async(
        self,
        request: main_models.CreateAppKeyRequest,
    ) -> main_models.CreateAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_app_key_with_options_async(request, runtime)

    def create_cust_variable_with_options(
        self,
        request: main_models.CreateCustVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.history_value_type):
            query['historyValueType'] = request.history_value_type
        if not DaraCore.is_null(request.object):
            query['object'] = request.object
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.subject):
            query['subject'] = request.subject
        if not DaraCore.is_null(request.time_type):
            query['timeType'] = request.time_type
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.tw_count):
            query['twCount'] = request.tw_count
        if not DaraCore.is_null(request.velocity_fc):
            query['velocityFC'] = request.velocity_fc
        if not DaraCore.is_null(request.velocity_tw):
            query['velocityTW'] = request.velocity_tw
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cust_variable_with_options_async(
        self,
        request: main_models.CreateCustVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.history_value_type):
            query['historyValueType'] = request.history_value_type
        if not DaraCore.is_null(request.object):
            query['object'] = request.object
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.subject):
            query['subject'] = request.subject
        if not DaraCore.is_null(request.time_type):
            query['timeType'] = request.time_type
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.tw_count):
            query['twCount'] = request.tw_count
        if not DaraCore.is_null(request.velocity_fc):
            query['velocityFC'] = request.velocity_fc
        if not DaraCore.is_null(request.velocity_tw):
            query['velocityTW'] = request.velocity_tw
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cust_variable(
        self,
        request: main_models.CreateCustVariableRequest,
    ) -> main_models.CreateCustVariableResponse:
        runtime = RuntimeOptions()
        return self.create_cust_variable_with_options(request, runtime)

    async def create_cust_variable_async(
        self,
        request: main_models.CreateCustVariableRequest,
    ) -> main_models.CreateCustVariableResponse:
        runtime = RuntimeOptions()
        return await self.create_cust_variable_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        request: main_models.CreateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.oss_key):
            query['ossKey'] = request.oss_key
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSource',
            version = '2021-09-10',
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
        request: main_models.CreateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.oss_key):
            query['ossKey'] = request.oss_key
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSource',
            version = '2021-09-10',
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

    def create_event_with_options(
        self,
        request: main_models.CreateEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.input_fields_str):
            query['inputFieldsStr'] = request.input_fields_str
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_code):
            query['templateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_with_options_async(
        self,
        request: main_models.CreateEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.input_fields_str):
            query['inputFieldsStr'] = request.input_fields_str
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_code):
            query['templateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event(
        self,
        request: main_models.CreateEventRequest,
    ) -> main_models.CreateEventResponse:
        runtime = RuntimeOptions()
        return self.create_event_with_options(request, runtime)

    async def create_event_async(
        self,
        request: main_models.CreateEventRequest,
    ) -> main_models.CreateEventResponse:
        runtime = RuntimeOptions()
        return await self.create_event_with_options_async(request, runtime)

    def create_expression_variable_with_options(
        self,
        request: main_models.CreateExpressionVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExpressionVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.outlier):
            query['outlier'] = request.outlier
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExpressionVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExpressionVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_expression_variable_with_options_async(
        self,
        request: main_models.CreateExpressionVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExpressionVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.outlier):
            query['outlier'] = request.outlier
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExpressionVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExpressionVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_expression_variable(
        self,
        request: main_models.CreateExpressionVariableRequest,
    ) -> main_models.CreateExpressionVariableResponse:
        runtime = RuntimeOptions()
        return self.create_expression_variable_with_options(request, runtime)

    async def create_expression_variable_async(
        self,
        request: main_models.CreateExpressionVariableRequest,
    ) -> main_models.CreateExpressionVariableResponse:
        runtime = RuntimeOptions()
        return await self.create_expression_variable_with_options_async(request, runtime)

    def create_field_with_options(
        self,
        request: main_models.CreateFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.classify):
            query['classify'] = request.classify
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.enum_data):
            query['enumData'] = request.enum_data
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_field_with_options_async(
        self,
        request: main_models.CreateFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.classify):
            query['classify'] = request.classify
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.enum_data):
            query['enumData'] = request.enum_data
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_field(
        self,
        request: main_models.CreateFieldRequest,
    ) -> main_models.CreateFieldResponse:
        runtime = RuntimeOptions()
        return self.create_field_with_options(request, runtime)

    async def create_field_async(
        self,
        request: main_models.CreateFieldRequest,
    ) -> main_models.CreateFieldResponse:
        runtime = RuntimeOptions()
        return await self.create_field_with_options_async(request, runtime)

    def create_model_with_options(
        self,
        request: main_models.CreateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buc_id):
            query['BucId'] = request.buc_id
        if not DaraCore.is_null(request.counts):
            query['Counts'] = request.counts
        if not DaraCore.is_null(request.file_md5):
            query['FileMD5'] = request.file_md5
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_scene):
            query['ModelScene'] = request.model_scene
        if not DaraCore.is_null(request.parameter_num):
            query['ParameterNum'] = request.parameter_num
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.user_local_file_name):
            query['UserLocalFileName'] = request.user_local_file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        request: main_models.CreateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buc_id):
            query['BucId'] = request.buc_id
        if not DaraCore.is_null(request.counts):
            query['Counts'] = request.counts
        if not DaraCore.is_null(request.file_md5):
            query['FileMD5'] = request.file_md5
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_scene):
            query['ModelScene'] = request.model_scene
        if not DaraCore.is_null(request.parameter_num):
            query['ParameterNum'] = request.parameter_num
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.user_local_file_name):
            query['UserLocalFileName'] = request.user_local_file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    async def create_model_async(
        self,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        return await self.create_model_with_options_async(request, runtime)

    def create_poc_ev_with_options(
        self,
        request: main_models.CreatePocEvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePocEvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date_format):
            query['DateFormat'] = request.date_format
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.tab):
            query['Tab'] = request.tab
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePocEv',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePocEvResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_poc_ev_with_options_async(
        self,
        request: main_models.CreatePocEvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePocEvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date_format):
            query['DateFormat'] = request.date_format
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.tab):
            query['Tab'] = request.tab
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePocEv',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePocEvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_poc_ev(
        self,
        request: main_models.CreatePocEvRequest,
    ) -> main_models.CreatePocEvResponse:
        runtime = RuntimeOptions()
        return self.create_poc_ev_with_options(request, runtime)

    async def create_poc_ev_async(
        self,
        request: main_models.CreatePocEvRequest,
    ) -> main_models.CreatePocEvResponse:
        runtime = RuntimeOptions()
        return await self.create_poc_ev_with_options_async(request, runtime)

    def create_query_variable_with_options(
        self,
        request: main_models.CreateQueryVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueryVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.outlier):
            query['outlier'] = request.outlier
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueryVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueryVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_query_variable_with_options_async(
        self,
        request: main_models.CreateQueryVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueryVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.outlier):
            query['outlier'] = request.outlier
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueryVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueryVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_query_variable(
        self,
        request: main_models.CreateQueryVariableRequest,
    ) -> main_models.CreateQueryVariableResponse:
        runtime = RuntimeOptions()
        return self.create_query_variable_with_options(request, runtime)

    async def create_query_variable_async(
        self,
        request: main_models.CreateQueryVariableRequest,
    ) -> main_models.CreateQueryVariableResponse:
        runtime = RuntimeOptions()
        return await self.create_query_variable_with_options_async(request, runtime)

    def create_recommend_event_rule_with_options(
        self,
        request: main_models.CreateRecommendEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecommendEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.recommend_rule_ids_str):
            query['recommendRuleIdsStr'] = request.recommend_rule_ids_str
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecommendEventRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecommendEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recommend_event_rule_with_options_async(
        self,
        request: main_models.CreateRecommendEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecommendEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.recommend_rule_ids_str):
            query['recommendRuleIdsStr'] = request.recommend_rule_ids_str
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecommendEventRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecommendEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recommend_event_rule(
        self,
        request: main_models.CreateRecommendEventRuleRequest,
    ) -> main_models.CreateRecommendEventRuleResponse:
        runtime = RuntimeOptions()
        return self.create_recommend_event_rule_with_options(request, runtime)

    async def create_recommend_event_rule_async(
        self,
        request: main_models.CreateRecommendEventRuleRequest,
    ) -> main_models.CreateRecommendEventRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_recommend_event_rule_with_options_async(request, runtime)

    def create_recommend_task_with_options(
        self,
        request: main_models.CreateRecommendTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecommendTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_id):
            query['sampleId'] = request.sample_id
        if not DaraCore.is_null(request.variables_str):
            query['variablesStr'] = request.variables_str
        if not DaraCore.is_null(request.velocities_str):
            query['velocitiesStr'] = request.velocities_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecommendTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecommendTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recommend_task_with_options_async(
        self,
        request: main_models.CreateRecommendTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecommendTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_id):
            query['sampleId'] = request.sample_id
        if not DaraCore.is_null(request.variables_str):
            query['variablesStr'] = request.variables_str
        if not DaraCore.is_null(request.velocities_str):
            query['velocitiesStr'] = request.velocities_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecommendTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecommendTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recommend_task(
        self,
        request: main_models.CreateRecommendTaskRequest,
    ) -> main_models.CreateRecommendTaskResponse:
        runtime = RuntimeOptions()
        return self.create_recommend_task_with_options(request, runtime)

    async def create_recommend_task_async(
        self,
        request: main_models.CreateRecommendTaskRequest,
    ) -> main_models.CreateRecommendTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_recommend_task_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.logic_expression):
            query['logicExpression'] = request.logic_expression
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_body):
            query['ruleBody'] = request.rule_body
        if not DaraCore.is_null(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['ruleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2021-09-10',
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
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.logic_expression):
            query['logicExpression'] = request.logic_expression
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_body):
            query['ruleBody'] = request.rule_body
        if not DaraCore.is_null(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['ruleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2021-09-10',
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

    def create_sample_with_options(
        self,
        request: main_models.CreateSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.client_file_name):
            query['clientFileName'] = request.client_file_name
        if not DaraCore.is_null(request.client_path):
            query['clientPath'] = request.client_path
        if not DaraCore.is_null(request.file_type):
            query['fileType'] = request.file_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_tag):
            query['sampleTag'] = request.sample_tag
        if not DaraCore.is_null(request.sample_type):
            query['sampleType'] = request.sample_type
        if not DaraCore.is_null(request.sample_values):
            query['sampleValues'] = request.sample_values
        if not DaraCore.is_null(request.upload_type):
            query['uploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSample',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_with_options_async(
        self,
        request: main_models.CreateSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.client_file_name):
            query['clientFileName'] = request.client_file_name
        if not DaraCore.is_null(request.client_path):
            query['clientPath'] = request.client_path
        if not DaraCore.is_null(request.file_type):
            query['fileType'] = request.file_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_tag):
            query['sampleTag'] = request.sample_tag
        if not DaraCore.is_null(request.sample_type):
            query['sampleType'] = request.sample_type
        if not DaraCore.is_null(request.sample_values):
            query['sampleValues'] = request.sample_values
        if not DaraCore.is_null(request.upload_type):
            query['uploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSample',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample(
        self,
        request: main_models.CreateSampleRequest,
    ) -> main_models.CreateSampleResponse:
        runtime = RuntimeOptions()
        return self.create_sample_with_options(request, runtime)

    async def create_sample_async(
        self,
        request: main_models.CreateSampleRequest,
    ) -> main_models.CreateSampleResponse:
        runtime = RuntimeOptions()
        return await self.create_sample_with_options_async(request, runtime)

    def create_sample_api_with_options(
        self,
        request: main_models.CreateSampleApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.data_value):
            query['DataValue'] = request.data_value
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.sample_batch_type):
            query['SampleBatchType'] = request.sample_batch_type
        if not DaraCore.is_null(request.service_list):
            query['ServiceList'] = request.service_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleApi',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_api_with_options_async(
        self,
        request: main_models.CreateSampleApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.data_value):
            query['DataValue'] = request.data_value
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.sample_batch_type):
            query['SampleBatchType'] = request.sample_batch_type
        if not DaraCore.is_null(request.service_list):
            query['ServiceList'] = request.service_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleApi',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample_api(
        self,
        request: main_models.CreateSampleApiRequest,
    ) -> main_models.CreateSampleApiResponse:
        runtime = RuntimeOptions()
        return self.create_sample_api_with_options(request, runtime)

    async def create_sample_api_async(
        self,
        request: main_models.CreateSampleApiRequest,
    ) -> main_models.CreateSampleApiResponse:
        runtime = RuntimeOptions()
        return await self.create_sample_api_with_options_async(request, runtime)

    def create_sample_batch_with_options(
        self,
        request: main_models.CreateSampleBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_name):
            query['batchName'] = request.batch_name
        if not DaraCore.is_null(request.data_type):
            query['dataType'] = request.data_type
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.oss_file_name):
            query['ossFileName'] = request.oss_file_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_batch_type):
            query['sampleBatchType'] = request.sample_batch_type
        if not DaraCore.is_null(request.service_list):
            query['serviceList'] = request.service_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleBatch',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_batch_with_options_async(
        self,
        request: main_models.CreateSampleBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_name):
            query['batchName'] = request.batch_name
        if not DaraCore.is_null(request.data_type):
            query['dataType'] = request.data_type
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.oss_file_name):
            query['ossFileName'] = request.oss_file_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_batch_type):
            query['sampleBatchType'] = request.sample_batch_type
        if not DaraCore.is_null(request.service_list):
            query['serviceList'] = request.service_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleBatch',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample_batch(
        self,
        request: main_models.CreateSampleBatchRequest,
    ) -> main_models.CreateSampleBatchResponse:
        runtime = RuntimeOptions()
        return self.create_sample_batch_with_options(request, runtime)

    async def create_sample_batch_async(
        self,
        request: main_models.CreateSampleBatchRequest,
    ) -> main_models.CreateSampleBatchResponse:
        runtime = RuntimeOptions()
        return await self.create_sample_batch_with_options_async(request, runtime)

    def create_sample_data_with_options(
        self,
        request: main_models.CreateSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.encrypt_type):
            query['encryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.risk_value):
            query['riskValue'] = request.risk_value
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        if not DaraCore.is_null(request.store_path):
            query['storePath'] = request.store_path
        if not DaraCore.is_null(request.store_type):
            query['storeType'] = request.store_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_data_with_options_async(
        self,
        request: main_models.CreateSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.encrypt_type):
            query['encryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.risk_value):
            query['riskValue'] = request.risk_value
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        if not DaraCore.is_null(request.store_path):
            query['storePath'] = request.store_path
        if not DaraCore.is_null(request.store_type):
            query['storeType'] = request.store_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample_data(
        self,
        request: main_models.CreateSampleDataRequest,
    ) -> main_models.CreateSampleDataResponse:
        runtime = RuntimeOptions()
        return self.create_sample_data_with_options(request, runtime)

    async def create_sample_data_async(
        self,
        request: main_models.CreateSampleDataRequest,
    ) -> main_models.CreateSampleDataResponse:
        runtime = RuntimeOptions()
        return await self.create_sample_data_with_options_async(request, runtime)

    def create_simulation_task_with_options(
        self,
        request: main_models.CreateSimulationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimulationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_config):
            query['dataSourceConfig'] = request.data_source_config
        if not DaraCore.is_null(request.data_source_type):
            query['dataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.filters_str):
            query['filtersStr'] = request.filters_str
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rules_str):
            query['rulesStr'] = request.rules_str
        if not DaraCore.is_null(request.run_task):
            query['runTask'] = request.run_task
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimulationTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimulationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_simulation_task_with_options_async(
        self,
        request: main_models.CreateSimulationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimulationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_config):
            query['dataSourceConfig'] = request.data_source_config
        if not DaraCore.is_null(request.data_source_type):
            query['dataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.filters_str):
            query['filtersStr'] = request.filters_str
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rules_str):
            query['rulesStr'] = request.rules_str
        if not DaraCore.is_null(request.run_task):
            query['runTask'] = request.run_task
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimulationTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimulationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_simulation_task(
        self,
        request: main_models.CreateSimulationTaskRequest,
    ) -> main_models.CreateSimulationTaskResponse:
        runtime = RuntimeOptions()
        return self.create_simulation_task_with_options(request, runtime)

    async def create_simulation_task_async(
        self,
        request: main_models.CreateSimulationTaskRequest,
    ) -> main_models.CreateSimulationTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_simulation_task_with_options_async(request, runtime)

    def deep_copy_rule_with_options(
        self,
        request: main_models.DeepCopyRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepCopyRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_type):
            query['CreateType'] = request.create_type
        if not DaraCore.is_null(request.cust_insert_info):
            query['CustInsertInfo'] = request.cust_insert_info
        if not DaraCore.is_null(request.cust_write_info):
            query['CustWriteInfo'] = request.cust_write_info
        if not DaraCore.is_null(request.expression_variable_info):
            query['ExpressionVariableInfo'] = request.expression_variable_info
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.query_expression_variable_info):
            query['QueryExpressionVariableInfo'] = request.query_expression_variable_info
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.source_rule_id):
            query['SourceRuleId'] = request.source_rule_id
        if not DaraCore.is_null(request.source_rule_ids):
            query['SourceRuleIds'] = request.source_rule_ids
        if not DaraCore.is_null(request.target_event_code):
            query['TargetEventCode'] = request.target_event_code
        if not DaraCore.is_null(request.target_event_name):
            query['TargetEventName'] = request.target_event_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeepCopyRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeepCopyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def deep_copy_rule_with_options_async(
        self,
        request: main_models.DeepCopyRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeepCopyRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_type):
            query['CreateType'] = request.create_type
        if not DaraCore.is_null(request.cust_insert_info):
            query['CustInsertInfo'] = request.cust_insert_info
        if not DaraCore.is_null(request.cust_write_info):
            query['CustWriteInfo'] = request.cust_write_info
        if not DaraCore.is_null(request.expression_variable_info):
            query['ExpressionVariableInfo'] = request.expression_variable_info
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.query_expression_variable_info):
            query['QueryExpressionVariableInfo'] = request.query_expression_variable_info
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.source_rule_id):
            query['SourceRuleId'] = request.source_rule_id
        if not DaraCore.is_null(request.source_rule_ids):
            query['SourceRuleIds'] = request.source_rule_ids
        if not DaraCore.is_null(request.target_event_code):
            query['TargetEventCode'] = request.target_event_code
        if not DaraCore.is_null(request.target_event_name):
            query['TargetEventName'] = request.target_event_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeepCopyRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeepCopyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deep_copy_rule(
        self,
        request: main_models.DeepCopyRuleRequest,
    ) -> main_models.DeepCopyRuleResponse:
        runtime = RuntimeOptions()
        return self.deep_copy_rule_with_options(request, runtime)

    async def deep_copy_rule_async(
        self,
        request: main_models.DeepCopyRuleRequest,
    ) -> main_models.DeepCopyRuleResponse:
        runtime = RuntimeOptions()
        return await self.deep_copy_rule_with_options_async(request, runtime)

    def delete_analysis_condition_favorite_with_options(
        self,
        request: main_models.DeleteAnalysisConditionFavoriteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnalysisConditionFavoriteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnalysisConditionFavorite',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnalysisConditionFavoriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_analysis_condition_favorite_with_options_async(
        self,
        request: main_models.DeleteAnalysisConditionFavoriteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnalysisConditionFavoriteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnalysisConditionFavorite',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnalysisConditionFavoriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_analysis_condition_favorite(
        self,
        request: main_models.DeleteAnalysisConditionFavoriteRequest,
    ) -> main_models.DeleteAnalysisConditionFavoriteResponse:
        runtime = RuntimeOptions()
        return self.delete_analysis_condition_favorite_with_options(request, runtime)

    async def delete_analysis_condition_favorite_async(
        self,
        request: main_models.DeleteAnalysisConditionFavoriteRequest,
    ) -> main_models.DeleteAnalysisConditionFavoriteResponse:
        runtime = RuntimeOptions()
        return await self.delete_analysis_condition_favorite_with_options_async(request, runtime)

    def delete_by_pass_shunt_event_with_options(
        self,
        request: main_models.DeleteByPassShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteByPassShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteByPassShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteByPassShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_by_pass_shunt_event_with_options_async(
        self,
        request: main_models.DeleteByPassShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteByPassShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteByPassShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteByPassShuntEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_by_pass_shunt_event(
        self,
        request: main_models.DeleteByPassShuntEventRequest,
    ) -> main_models.DeleteByPassShuntEventResponse:
        runtime = RuntimeOptions()
        return self.delete_by_pass_shunt_event_with_options(request, runtime)

    async def delete_by_pass_shunt_event_async(
        self,
        request: main_models.DeleteByPassShuntEventRequest,
    ) -> main_models.DeleteByPassShuntEventResponse:
        runtime = RuntimeOptions()
        return await self.delete_by_pass_shunt_event_with_options_async(request, runtime)

    def delete_cust_variable_with_options(
        self,
        request: main_models.DeleteCustVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cust_variable_with_options_async(
        self,
        request: main_models.DeleteCustVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cust_variable(
        self,
        request: main_models.DeleteCustVariableRequest,
    ) -> main_models.DeleteCustVariableResponse:
        runtime = RuntimeOptions()
        return self.delete_cust_variable_with_options(request, runtime)

    async def delete_cust_variable_async(
        self,
        request: main_models.DeleteCustVariableRequest,
    ) -> main_models.DeleteCustVariableResponse:
        runtime = RuntimeOptions()
        return await self.delete_cust_variable_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2021-09-10',
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
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2021-09-10',
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

    def delete_event_field_with_options(
        self,
        request: main_models.DeleteEventFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_field_with_options_async(
        self,
        request: main_models.DeleteEventFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_field(
        self,
        request: main_models.DeleteEventFieldRequest,
    ) -> main_models.DeleteEventFieldResponse:
        runtime = RuntimeOptions()
        return self.delete_event_field_with_options(request, runtime)

    async def delete_event_field_async(
        self,
        request: main_models.DeleteEventFieldRequest,
    ) -> main_models.DeleteEventFieldResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_field_with_options_async(request, runtime)

    def delete_expression_variable_with_options(
        self,
        request: main_models.DeleteExpressionVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExpressionVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExpressionVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExpressionVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_expression_variable_with_options_async(
        self,
        request: main_models.DeleteExpressionVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExpressionVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExpressionVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExpressionVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_expression_variable(
        self,
        request: main_models.DeleteExpressionVariableRequest,
    ) -> main_models.DeleteExpressionVariableResponse:
        runtime = RuntimeOptions()
        return self.delete_expression_variable_with_options(request, runtime)

    async def delete_expression_variable_async(
        self,
        request: main_models.DeleteExpressionVariableRequest,
    ) -> main_models.DeleteExpressionVariableResponse:
        runtime = RuntimeOptions()
        return await self.delete_expression_variable_with_options_async(request, runtime)

    def delete_field_with_options(
        self,
        request: main_models.DeleteFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_field_with_options_async(
        self,
        request: main_models.DeleteFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_field(
        self,
        request: main_models.DeleteFieldRequest,
    ) -> main_models.DeleteFieldResponse:
        runtime = RuntimeOptions()
        return self.delete_field_with_options(request, runtime)

    async def delete_field_async(
        self,
        request: main_models.DeleteFieldRequest,
    ) -> main_models.DeleteFieldResponse:
        runtime = RuntimeOptions()
        return await self.delete_field_with_options_async(request, runtime)

    def delete_name_list_with_options(
        self,
        request: main_models.DeleteNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.ids):
            query['ids'] = request.ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_name_list_with_options_async(
        self,
        request: main_models.DeleteNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.ids):
            query['ids'] = request.ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_name_list(
        self,
        request: main_models.DeleteNameListRequest,
    ) -> main_models.DeleteNameListResponse:
        runtime = RuntimeOptions()
        return self.delete_name_list_with_options(request, runtime)

    async def delete_name_list_async(
        self,
        request: main_models.DeleteNameListRequest,
    ) -> main_models.DeleteNameListResponse:
        runtime = RuntimeOptions()
        return await self.delete_name_list_with_options_async(request, runtime)

    def delete_name_list_data_with_options(
        self,
        request: main_models.DeleteNameListDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNameListDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNameListData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNameListDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_name_list_data_with_options_async(
        self,
        request: main_models.DeleteNameListDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNameListDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNameListData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNameListDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_name_list_data(
        self,
        request: main_models.DeleteNameListDataRequest,
    ) -> main_models.DeleteNameListDataResponse:
        runtime = RuntimeOptions()
        return self.delete_name_list_data_with_options(request, runtime)

    async def delete_name_list_data_async(
        self,
        request: main_models.DeleteNameListDataRequest,
    ) -> main_models.DeleteNameListDataResponse:
        runtime = RuntimeOptions()
        return await self.delete_name_list_data_with_options_async(request, runtime)

    def delete_query_variable_with_options(
        self,
        request: main_models.DeleteQueryVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueryVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueryVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueryVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_query_variable_with_options_async(
        self,
        request: main_models.DeleteQueryVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueryVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueryVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueryVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_query_variable(
        self,
        request: main_models.DeleteQueryVariableRequest,
    ) -> main_models.DeleteQueryVariableResponse:
        runtime = RuntimeOptions()
        return self.delete_query_variable_with_options(request, runtime)

    async def delete_query_variable_async(
        self,
        request: main_models.DeleteQueryVariableRequest,
    ) -> main_models.DeleteQueryVariableResponse:
        runtime = RuntimeOptions()
        return await self.delete_query_variable_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2021-09-10',
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
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2021-09-10',
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

    def delete_sample_batch_with_options(
        self,
        request: main_models.DeleteSampleBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSampleBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.ids):
            query['ids'] = request.ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.versions):
            query['versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSampleBatch',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSampleBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sample_batch_with_options_async(
        self,
        request: main_models.DeleteSampleBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSampleBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.ids):
            query['ids'] = request.ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.versions):
            query['versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSampleBatch',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSampleBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sample_batch(
        self,
        request: main_models.DeleteSampleBatchRequest,
    ) -> main_models.DeleteSampleBatchResponse:
        runtime = RuntimeOptions()
        return self.delete_sample_batch_with_options(request, runtime)

    async def delete_sample_batch_async(
        self,
        request: main_models.DeleteSampleBatchRequest,
    ) -> main_models.DeleteSampleBatchResponse:
        runtime = RuntimeOptions()
        return await self.delete_sample_batch_with_options_async(request, runtime)

    def delete_sample_batch_meta_with_options(
        self,
        request: main_models.DeleteSampleBatchMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSampleBatchMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_uuid):
            query['batchUuid'] = request.batch_uuid
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSampleBatchMeta',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSampleBatchMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sample_batch_meta_with_options_async(
        self,
        request: main_models.DeleteSampleBatchMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSampleBatchMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_uuid):
            query['batchUuid'] = request.batch_uuid
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSampleBatchMeta',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSampleBatchMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sample_batch_meta(
        self,
        request: main_models.DeleteSampleBatchMetaRequest,
    ) -> main_models.DeleteSampleBatchMetaResponse:
        runtime = RuntimeOptions()
        return self.delete_sample_batch_meta_with_options(request, runtime)

    async def delete_sample_batch_meta_async(
        self,
        request: main_models.DeleteSampleBatchMetaRequest,
    ) -> main_models.DeleteSampleBatchMetaResponse:
        runtime = RuntimeOptions()
        return await self.delete_sample_batch_meta_with_options_async(request, runtime)

    def delete_sample_data_with_options(
        self,
        request: main_models.DeleteSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSampleData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sample_data_with_options_async(
        self,
        request: main_models.DeleteSampleDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSampleDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSampleData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sample_data(
        self,
        request: main_models.DeleteSampleDataRequest,
    ) -> main_models.DeleteSampleDataResponse:
        runtime = RuntimeOptions()
        return self.delete_sample_data_with_options(request, runtime)

    async def delete_sample_data_async(
        self,
        request: main_models.DeleteSampleDataRequest,
    ) -> main_models.DeleteSampleDataResponse:
        runtime = RuntimeOptions()
        return await self.delete_sample_data_with_options_async(request, runtime)

    def delete_self_bind_variable_with_options(
        self,
        request: main_models.DeleteSelfBindVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSelfBindVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSelfBindVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSelfBindVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_self_bind_variable_with_options_async(
        self,
        request: main_models.DeleteSelfBindVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSelfBindVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSelfBindVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSelfBindVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_self_bind_variable(
        self,
        request: main_models.DeleteSelfBindVariableRequest,
    ) -> main_models.DeleteSelfBindVariableResponse:
        runtime = RuntimeOptions()
        return self.delete_self_bind_variable_with_options(request, runtime)

    async def delete_self_bind_variable_async(
        self,
        request: main_models.DeleteSelfBindVariableRequest,
    ) -> main_models.DeleteSelfBindVariableResponse:
        runtime = RuntimeOptions()
        return await self.delete_self_bind_variable_with_options_async(request, runtime)

    def describe_advance_search_left_variable_list_with_options(
        self,
        request: main_models.DescribeAdvanceSearchLeftVariableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvanceSearchLeftVariableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvanceSearchLeftVariableList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvanceSearchLeftVariableListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advance_search_left_variable_list_with_options_async(
        self,
        request: main_models.DescribeAdvanceSearchLeftVariableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvanceSearchLeftVariableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvanceSearchLeftVariableList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvanceSearchLeftVariableListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advance_search_left_variable_list(
        self,
        request: main_models.DescribeAdvanceSearchLeftVariableListRequest,
    ) -> main_models.DescribeAdvanceSearchLeftVariableListResponse:
        runtime = RuntimeOptions()
        return self.describe_advance_search_left_variable_list_with_options(request, runtime)

    async def describe_advance_search_left_variable_list_async(
        self,
        request: main_models.DescribeAdvanceSearchLeftVariableListRequest,
    ) -> main_models.DescribeAdvanceSearchLeftVariableListResponse:
        runtime = RuntimeOptions()
        return await self.describe_advance_search_left_variable_list_with_options_async(request, runtime)

    def describe_advance_search_page_list_with_options(
        self,
        request: main_models.DescribeAdvanceSearchPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvanceSearchPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvanceSearchPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvanceSearchPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advance_search_page_list_with_options_async(
        self,
        request: main_models.DescribeAdvanceSearchPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvanceSearchPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvanceSearchPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvanceSearchPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advance_search_page_list(
        self,
        request: main_models.DescribeAdvanceSearchPageListRequest,
    ) -> main_models.DescribeAdvanceSearchPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_advance_search_page_list_with_options(request, runtime)

    async def describe_advance_search_page_list_async(
        self,
        request: main_models.DescribeAdvanceSearchPageListRequest,
    ) -> main_models.DescribeAdvanceSearchPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_advance_search_page_list_with_options_async(request, runtime)

    def describe_all_data_source_with_options(
        self,
        request: main_models.DescribeAllDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSource',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_source_with_options_async(
        self,
        request: main_models.DescribeAllDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSource',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_source(
        self,
        request: main_models.DescribeAllDataSourceRequest,
    ) -> main_models.DescribeAllDataSourceResponse:
        runtime = RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    async def describe_all_data_source_async(
        self,
        request: main_models.DescribeAllDataSourceRequest,
    ) -> main_models.DescribeAllDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_data_source_with_options_async(request, runtime)

    def describe_all_event_name_and_code_with_options(
        self,
        request: main_models.DescribeAllEventNameAndCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllEventNameAndCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllEventNameAndCode',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllEventNameAndCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_event_name_and_code_with_options_async(
        self,
        request: main_models.DescribeAllEventNameAndCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllEventNameAndCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllEventNameAndCode',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllEventNameAndCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_event_name_and_code(
        self,
        request: main_models.DescribeAllEventNameAndCodeRequest,
    ) -> main_models.DescribeAllEventNameAndCodeResponse:
        runtime = RuntimeOptions()
        return self.describe_all_event_name_and_code_with_options(request, runtime)

    async def describe_all_event_name_and_code_async(
        self,
        request: main_models.DescribeAllEventNameAndCodeRequest,
    ) -> main_models.DescribeAllEventNameAndCodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_event_name_and_code_with_options_async(request, runtime)

    def describe_all_root_variable_with_options(
        self,
        request: main_models.DescribeAllRootVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllRootVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.device_variable_ids):
            query['deviceVariableIds'] = request.device_variable_ids
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression_variable_ids):
            query['expressionVariableIds'] = request.expression_variable_ids
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.native_variable_ids):
            query['nativeVariableIds'] = request.native_variable_ids
        if not DaraCore.is_null(request.query_variable_ids):
            query['queryVariableIds'] = request.query_variable_ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.velocity_variable_ids):
            query['velocityVariableIds'] = request.velocity_variable_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllRootVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllRootVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_root_variable_with_options_async(
        self,
        request: main_models.DescribeAllRootVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllRootVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.device_variable_ids):
            query['deviceVariableIds'] = request.device_variable_ids
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression_variable_ids):
            query['expressionVariableIds'] = request.expression_variable_ids
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.native_variable_ids):
            query['nativeVariableIds'] = request.native_variable_ids
        if not DaraCore.is_null(request.query_variable_ids):
            query['queryVariableIds'] = request.query_variable_ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.velocity_variable_ids):
            query['velocityVariableIds'] = request.velocity_variable_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllRootVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllRootVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_root_variable(
        self,
        request: main_models.DescribeAllRootVariableRequest,
    ) -> main_models.DescribeAllRootVariableResponse:
        runtime = RuntimeOptions()
        return self.describe_all_root_variable_with_options(request, runtime)

    async def describe_all_root_variable_async(
        self,
        request: main_models.DescribeAllRootVariableRequest,
    ) -> main_models.DescribeAllRootVariableResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_root_variable_with_options_async(request, runtime)

    def describe_analysis_column_field_list_with_options(
        self,
        request: main_models.DescribeAnalysisColumnFieldListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAnalysisColumnFieldListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAnalysisColumnFieldList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAnalysisColumnFieldListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_analysis_column_field_list_with_options_async(
        self,
        request: main_models.DescribeAnalysisColumnFieldListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAnalysisColumnFieldListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAnalysisColumnFieldList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAnalysisColumnFieldListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_analysis_column_field_list(
        self,
        request: main_models.DescribeAnalysisColumnFieldListRequest,
    ) -> main_models.DescribeAnalysisColumnFieldListResponse:
        runtime = RuntimeOptions()
        return self.describe_analysis_column_field_list_with_options(request, runtime)

    async def describe_analysis_column_field_list_async(
        self,
        request: main_models.DescribeAnalysisColumnFieldListRequest,
    ) -> main_models.DescribeAnalysisColumnFieldListResponse:
        runtime = RuntimeOptions()
        return await self.describe_analysis_column_field_list_with_options_async(request, runtime)

    def describe_analysis_column_list_with_options(
        self,
        request: main_models.DescribeAnalysisColumnListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAnalysisColumnListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAnalysisColumnList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAnalysisColumnListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_analysis_column_list_with_options_async(
        self,
        request: main_models.DescribeAnalysisColumnListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAnalysisColumnListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAnalysisColumnList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAnalysisColumnListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_analysis_column_list(
        self,
        request: main_models.DescribeAnalysisColumnListRequest,
    ) -> main_models.DescribeAnalysisColumnListResponse:
        runtime = RuntimeOptions()
        return self.describe_analysis_column_list_with_options(request, runtime)

    async def describe_analysis_column_list_async(
        self,
        request: main_models.DescribeAnalysisColumnListRequest,
    ) -> main_models.DescribeAnalysisColumnListResponse:
        runtime = RuntimeOptions()
        return await self.describe_analysis_column_list_with_options_async(request, runtime)

    def describe_analysis_condition_favorite_list_with_options(
        self,
        request: main_models.DescribeAnalysisConditionFavoriteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAnalysisConditionFavoriteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAnalysisConditionFavoriteList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAnalysisConditionFavoriteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_analysis_condition_favorite_list_with_options_async(
        self,
        request: main_models.DescribeAnalysisConditionFavoriteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAnalysisConditionFavoriteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAnalysisConditionFavoriteList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAnalysisConditionFavoriteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_analysis_condition_favorite_list(
        self,
        request: main_models.DescribeAnalysisConditionFavoriteListRequest,
    ) -> main_models.DescribeAnalysisConditionFavoriteListResponse:
        runtime = RuntimeOptions()
        return self.describe_analysis_condition_favorite_list_with_options(request, runtime)

    async def describe_analysis_condition_favorite_list_async(
        self,
        request: main_models.DescribeAnalysisConditionFavoriteListRequest,
    ) -> main_models.DescribeAnalysisConditionFavoriteListResponse:
        runtime = RuntimeOptions()
        return await self.describe_analysis_condition_favorite_list_with_options_async(request, runtime)

    def describe_analysis_export_task_download_url_with_options(
        self,
        request: main_models.DescribeAnalysisExportTaskDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAnalysisExportTaskDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAnalysisExportTaskDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAnalysisExportTaskDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_analysis_export_task_download_url_with_options_async(
        self,
        request: main_models.DescribeAnalysisExportTaskDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAnalysisExportTaskDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAnalysisExportTaskDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAnalysisExportTaskDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_analysis_export_task_download_url(
        self,
        request: main_models.DescribeAnalysisExportTaskDownloadUrlRequest,
    ) -> main_models.DescribeAnalysisExportTaskDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_analysis_export_task_download_url_with_options(request, runtime)

    async def describe_analysis_export_task_download_url_async(
        self,
        request: main_models.DescribeAnalysisExportTaskDownloadUrlRequest,
    ) -> main_models.DescribeAnalysisExportTaskDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_analysis_export_task_download_url_with_options_async(request, runtime)

    def describe_api_with_options(
        self,
        request: main_models.DescribeApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.api_id):
            query['apiId'] = request.api_id
        if not DaraCore.is_null(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not DaraCore.is_null(request.api_type):
            query['apiType'] = request.api_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApi',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_with_options_async(
        self,
        request: main_models.DescribeApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.api_id):
            query['apiId'] = request.api_id
        if not DaraCore.is_null(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not DaraCore.is_null(request.api_type):
            query['apiType'] = request.api_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApi',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api(
        self,
        request: main_models.DescribeApiRequest,
    ) -> main_models.DescribeApiResponse:
        runtime = RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    async def describe_api_async(
        self,
        request: main_models.DescribeApiRequest,
    ) -> main_models.DescribeApiResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_with_options_async(request, runtime)

    def describe_api_groups_with_options(
        self,
        request: main_models.DescribeApiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiGroups',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_groups_with_options_async(
        self,
        request: main_models.DescribeApiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiGroups',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_groups(
        self,
        request: main_models.DescribeApiGroupsRequest,
    ) -> main_models.DescribeApiGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    async def describe_api_groups_async(
        self,
        request: main_models.DescribeApiGroupsRequest,
    ) -> main_models.DescribeApiGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_groups_with_options_async(request, runtime)

    def describe_api_limit_with_options(
        self,
        request: main_models.DescribeApiLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_limit_with_options_async(
        self,
        request: main_models.DescribeApiLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_limit(
        self,
        request: main_models.DescribeApiLimitRequest,
    ) -> main_models.DescribeApiLimitResponse:
        runtime = RuntimeOptions()
        return self.describe_api_limit_with_options(request, runtime)

    async def describe_api_limit_async(
        self,
        request: main_models.DescribeApiLimitRequest,
    ) -> main_models.DescribeApiLimitResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_limit_with_options_async(request, runtime)

    def describe_api_name_list_with_options(
        self,
        request: main_models.DescribeApiNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_name_list_with_options_async(
        self,
        request: main_models.DescribeApiNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_name_list(
        self,
        request: main_models.DescribeApiNameListRequest,
    ) -> main_models.DescribeApiNameListResponse:
        runtime = RuntimeOptions()
        return self.describe_api_name_list_with_options(request, runtime)

    async def describe_api_name_list_async(
        self,
        request: main_models.DescribeApiNameListRequest,
    ) -> main_models.DescribeApiNameListResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_name_list_with_options_async(request, runtime)

    def describe_api_variable_with_options(
        self,
        request: main_models.DescribeApiVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_variable_with_options_async(
        self,
        request: main_models.DescribeApiVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_variable(
        self,
        request: main_models.DescribeApiVariableRequest,
    ) -> main_models.DescribeApiVariableResponse:
        runtime = RuntimeOptions()
        return self.describe_api_variable_with_options(request, runtime)

    async def describe_api_variable_async(
        self,
        request: main_models.DescribeApiVariableRequest,
    ) -> main_models.DescribeApiVariableResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_variable_with_options_async(request, runtime)

    def describe_apis_with_options(
        self,
        request: main_models.DescribeApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.api_group_id):
            query['apiGroupId'] = request.api_group_id
        if not DaraCore.is_null(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not DaraCore.is_null(request.api_type):
            query['apiType'] = request.api_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApis',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_with_options_async(
        self,
        request: main_models.DescribeApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.api_group_id):
            query['apiGroupId'] = request.api_group_id
        if not DaraCore.is_null(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not DaraCore.is_null(request.api_type):
            query['apiType'] = request.api_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApis',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis(
        self,
        request: main_models.DescribeApisRequest,
    ) -> main_models.DescribeApisResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    async def describe_apis_async(
        self,
        request: main_models.DescribeApisRequest,
    ) -> main_models.DescribeApisResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_with_options_async(request, runtime)

    def describe_app_key_page_with_options(
        self,
        request: main_models.DescribeAppKeyPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppKeyPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppKeyPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppKeyPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_key_page_with_options_async(
        self,
        request: main_models.DescribeAppKeyPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppKeyPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppKeyPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppKeyPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_key_page(
        self,
        request: main_models.DescribeAppKeyPageRequest,
    ) -> main_models.DescribeAppKeyPageResponse:
        runtime = RuntimeOptions()
        return self.describe_app_key_page_with_options(request, runtime)

    async def describe_app_key_page_async(
        self,
        request: main_models.DescribeAppKeyPageRequest,
    ) -> main_models.DescribeAppKeyPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_key_page_with_options_async(request, runtime)

    def describe_audit_config_with_options(
        self,
        request: main_models.DescribeAuditConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.audit_relation_type):
            query['auditRelationType'] = request.audit_relation_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditConfig',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_config_with_options_async(
        self,
        request: main_models.DescribeAuditConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.audit_relation_type):
            query['auditRelationType'] = request.audit_relation_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditConfig',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_config(
        self,
        request: main_models.DescribeAuditConfigRequest,
    ) -> main_models.DescribeAuditConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_config_with_options(request, runtime)

    async def describe_audit_config_async(
        self,
        request: main_models.DescribeAuditConfigRequest,
    ) -> main_models.DescribeAuditConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_config_with_options_async(request, runtime)

    def describe_audit_details_with_options(
        self,
        request: main_models.DescribeAuditDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditDetails',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_details_with_options_async(
        self,
        request: main_models.DescribeAuditDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditDetails',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_details(
        self,
        request: main_models.DescribeAuditDetailsRequest,
    ) -> main_models.DescribeAuditDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_details_with_options(request, runtime)

    async def describe_audit_details_async(
        self,
        request: main_models.DescribeAuditDetailsRequest,
    ) -> main_models.DescribeAuditDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_details_with_options_async(request, runtime)

    def describe_audit_page_list_with_options(
        self,
        request: main_models.DescribeAuditPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.audit_status):
            query['auditStatus'] = request.audit_status
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_page_list_with_options_async(
        self,
        request: main_models.DescribeAuditPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.audit_status):
            query['auditStatus'] = request.audit_status
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_page_list(
        self,
        request: main_models.DescribeAuditPageListRequest,
    ) -> main_models.DescribeAuditPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_page_list_with_options(request, runtime)

    async def describe_audit_page_list_async(
        self,
        request: main_models.DescribeAuditPageListRequest,
    ) -> main_models.DescribeAuditPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_page_list_with_options_async(request, runtime)

    def describe_auth_event_name_list_with_options(
        self,
        request: main_models.DescribeAuthEventNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthEventNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthEventNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthEventNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auth_event_name_list_with_options_async(
        self,
        request: main_models.DescribeAuthEventNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthEventNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthEventNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthEventNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auth_event_name_list(
        self,
        request: main_models.DescribeAuthEventNameListRequest,
    ) -> main_models.DescribeAuthEventNameListResponse:
        runtime = RuntimeOptions()
        return self.describe_auth_event_name_list_with_options(request, runtime)

    async def describe_auth_event_name_list_async(
        self,
        request: main_models.DescribeAuthEventNameListRequest,
    ) -> main_models.DescribeAuthEventNameListResponse:
        runtime = RuntimeOptions()
        return await self.describe_auth_event_name_list_with_options_async(request, runtime)

    def describe_auth_rule_page_list_with_options(
        self,
        request: main_models.DescribeAuthRulePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthRulePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthRulePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthRulePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auth_rule_page_list_with_options_async(
        self,
        request: main_models.DescribeAuthRulePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthRulePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthRulePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthRulePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auth_rule_page_list(
        self,
        request: main_models.DescribeAuthRulePageListRequest,
    ) -> main_models.DescribeAuthRulePageListResponse:
        runtime = RuntimeOptions()
        return self.describe_auth_rule_page_list_with_options(request, runtime)

    async def describe_auth_rule_page_list_async(
        self,
        request: main_models.DescribeAuthRulePageListRequest,
    ) -> main_models.DescribeAuthRulePageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_auth_rule_page_list_with_options_async(request, runtime)

    def describe_auth_scene_list_with_options(
        self,
        request: main_models.DescribeAuthSceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthSceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthSceneList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auth_scene_list_with_options_async(
        self,
        request: main_models.DescribeAuthSceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthSceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthSceneList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auth_scene_list(
        self,
        request: main_models.DescribeAuthSceneListRequest,
    ) -> main_models.DescribeAuthSceneListResponse:
        runtime = RuntimeOptions()
        return self.describe_auth_scene_list_with_options(request, runtime)

    async def describe_auth_scene_list_async(
        self,
        request: main_models.DescribeAuthSceneListRequest,
    ) -> main_models.DescribeAuthSceneListResponse:
        runtime = RuntimeOptions()
        return await self.describe_auth_scene_list_with_options_async(request, runtime)

    def describe_auth_scene_page_list_with_options(
        self,
        request: main_models.DescribeAuthScenePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthScenePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene_name):
            query['sceneName'] = request.scene_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthScenePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthScenePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auth_scene_page_list_with_options_async(
        self,
        request: main_models.DescribeAuthScenePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthScenePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene_name):
            query['sceneName'] = request.scene_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthScenePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthScenePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auth_scene_page_list(
        self,
        request: main_models.DescribeAuthScenePageListRequest,
    ) -> main_models.DescribeAuthScenePageListResponse:
        runtime = RuntimeOptions()
        return self.describe_auth_scene_page_list_with_options(request, runtime)

    async def describe_auth_scene_page_list_async(
        self,
        request: main_models.DescribeAuthScenePageListRequest,
    ) -> main_models.DescribeAuthScenePageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_auth_scene_page_list_with_options_async(request, runtime)

    def describe_auth_status_with_options(
        self,
        request: main_models.DescribeAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthStatus',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auth_status_with_options_async(
        self,
        request: main_models.DescribeAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthStatus',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auth_status(
        self,
        request: main_models.DescribeAuthStatusRequest,
    ) -> main_models.DescribeAuthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_auth_status_with_options(request, runtime)

    async def describe_auth_status_async(
        self,
        request: main_models.DescribeAuthStatusRequest,
    ) -> main_models.DescribeAuthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_auth_status_with_options_async(request, runtime)

    def describe_avg_execute_cost_report_with_options(
        self,
        request: main_models.DescribeAvgExecuteCostReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvgExecuteCostReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvgExecuteCostReport',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvgExecuteCostReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_avg_execute_cost_report_with_options_async(
        self,
        request: main_models.DescribeAvgExecuteCostReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvgExecuteCostReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvgExecuteCostReport',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvgExecuteCostReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_avg_execute_cost_report(
        self,
        request: main_models.DescribeAvgExecuteCostReportRequest,
    ) -> main_models.DescribeAvgExecuteCostReportResponse:
        runtime = RuntimeOptions()
        return self.describe_avg_execute_cost_report_with_options(request, runtime)

    async def describe_avg_execute_cost_report_async(
        self,
        request: main_models.DescribeAvgExecuteCostReportRequest,
    ) -> main_models.DescribeAvgExecuteCostReportResponse:
        runtime = RuntimeOptions()
        return await self.describe_avg_execute_cost_report_with_options_async(request, runtime)

    def describe_basic_search_page_list_with_options(
        self,
        request: main_models.DescribeBasicSearchPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBasicSearchPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBasicSearchPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBasicSearchPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_basic_search_page_list_with_options_async(
        self,
        request: main_models.DescribeBasicSearchPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBasicSearchPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBasicSearchPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBasicSearchPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_basic_search_page_list(
        self,
        request: main_models.DescribeBasicSearchPageListRequest,
    ) -> main_models.DescribeBasicSearchPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_basic_search_page_list_with_options(request, runtime)

    async def describe_basic_search_page_list_async(
        self,
        request: main_models.DescribeBasicSearchPageListRequest,
    ) -> main_models.DescribeBasicSearchPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_basic_search_page_list_with_options_async(request, runtime)

    def describe_basic_start_with_options(
        self,
        request: main_models.DescribeBasicStartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBasicStartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['appKey'] = request.app_key
        if not DaraCore.is_null(request.end_ds):
            query['endDs'] = request.end_ds
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.service):
            query['service'] = request.service
        if not DaraCore.is_null(request.start_ds):
            query['startDs'] = request.start_ds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBasicStart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBasicStartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_basic_start_with_options_async(
        self,
        request: main_models.DescribeBasicStartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBasicStartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['appKey'] = request.app_key
        if not DaraCore.is_null(request.end_ds):
            query['endDs'] = request.end_ds
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.service):
            query['service'] = request.service
        if not DaraCore.is_null(request.start_ds):
            query['startDs'] = request.start_ds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBasicStart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBasicStartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_basic_start(
        self,
        request: main_models.DescribeBasicStartRequest,
    ) -> main_models.DescribeBasicStartResponse:
        runtime = RuntimeOptions()
        return self.describe_basic_start_with_options(request, runtime)

    async def describe_basic_start_async(
        self,
        request: main_models.DescribeBasicStartRequest,
    ) -> main_models.DescribeBasicStartResponse:
        runtime = RuntimeOptions()
        return await self.describe_basic_start_with_options_async(request, runtime)

    def describe_by_pass_shunt_event_with_options(
        self,
        request: main_models.DescribeByPassShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeByPassShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeByPassShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeByPassShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_by_pass_shunt_event_with_options_async(
        self,
        request: main_models.DescribeByPassShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeByPassShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeByPassShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeByPassShuntEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_by_pass_shunt_event(
        self,
        request: main_models.DescribeByPassShuntEventRequest,
    ) -> main_models.DescribeByPassShuntEventResponse:
        runtime = RuntimeOptions()
        return self.describe_by_pass_shunt_event_with_options(request, runtime)

    async def describe_by_pass_shunt_event_async(
        self,
        request: main_models.DescribeByPassShuntEventRequest,
    ) -> main_models.DescribeByPassShuntEventResponse:
        runtime = RuntimeOptions()
        return await self.describe_by_pass_shunt_event_with_options_async(request, runtime)

    def describe_cust_variable_config_list_with_options(
        self,
        request: main_models.DescribeCustVariableConfigListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustVariableConfigListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.biz_type):
            query['bizType'] = request.biz_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.time_type):
            query['timeType'] = request.time_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustVariableConfigList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustVariableConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cust_variable_config_list_with_options_async(
        self,
        request: main_models.DescribeCustVariableConfigListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustVariableConfigListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.biz_type):
            query['bizType'] = request.biz_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.time_type):
            query['timeType'] = request.time_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustVariableConfigList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustVariableConfigListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cust_variable_config_list(
        self,
        request: main_models.DescribeCustVariableConfigListRequest,
    ) -> main_models.DescribeCustVariableConfigListResponse:
        runtime = RuntimeOptions()
        return self.describe_cust_variable_config_list_with_options(request, runtime)

    async def describe_cust_variable_config_list_async(
        self,
        request: main_models.DescribeCustVariableConfigListRequest,
    ) -> main_models.DescribeCustVariableConfigListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cust_variable_config_list_with_options_async(request, runtime)

    def describe_cust_variable_detail_with_options(
        self,
        request: main_models.DescribeCustVariableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustVariableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustVariableDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustVariableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cust_variable_detail_with_options_async(
        self,
        request: main_models.DescribeCustVariableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustVariableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustVariableDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustVariableDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cust_variable_detail(
        self,
        request: main_models.DescribeCustVariableDetailRequest,
    ) -> main_models.DescribeCustVariableDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_cust_variable_detail_with_options(request, runtime)

    async def describe_cust_variable_detail_async(
        self,
        request: main_models.DescribeCustVariableDetailRequest,
    ) -> main_models.DescribeCustVariableDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_cust_variable_detail_with_options_async(request, runtime)

    def describe_cust_variable_page_with_options(
        self,
        request: main_models.DescribeCustVariablePageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustVariablePageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustVariablePage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustVariablePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cust_variable_page_with_options_async(
        self,
        request: main_models.DescribeCustVariablePageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustVariablePageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustVariablePage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustVariablePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cust_variable_page(
        self,
        request: main_models.DescribeCustVariablePageRequest,
    ) -> main_models.DescribeCustVariablePageResponse:
        runtime = RuntimeOptions()
        return self.describe_cust_variable_page_with_options(request, runtime)

    async def describe_cust_variable_page_async(
        self,
        request: main_models.DescribeCustVariablePageRequest,
    ) -> main_models.DescribeCustVariablePageResponse:
        runtime = RuntimeOptions()
        return await self.describe_cust_variable_page_with_options_async(request, runtime)

    def describe_data_source_data_download_url_with_options(
        self,
        request: main_models.DescribeDataSourceDataDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourceDataDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourceDataDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourceDataDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_source_data_download_url_with_options_async(
        self,
        request: main_models.DescribeDataSourceDataDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourceDataDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourceDataDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourceDataDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_source_data_download_url(
        self,
        request: main_models.DescribeDataSourceDataDownloadUrlRequest,
    ) -> main_models.DescribeDataSourceDataDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_data_source_data_download_url_with_options(request, runtime)

    async def describe_data_source_data_download_url_async(
        self,
        request: main_models.DescribeDataSourceDataDownloadUrlRequest,
    ) -> main_models.DescribeDataSourceDataDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_source_data_download_url_with_options_async(request, runtime)

    def describe_data_source_fields_with_options(
        self,
        request: main_models.DescribeDataSourceFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourceFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourceFields',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourceFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_source_fields_with_options_async(
        self,
        request: main_models.DescribeDataSourceFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourceFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourceFields',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourceFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_source_fields(
        self,
        request: main_models.DescribeDataSourceFieldsRequest,
    ) -> main_models.DescribeDataSourceFieldsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_source_fields_with_options(request, runtime)

    async def describe_data_source_fields_async(
        self,
        request: main_models.DescribeDataSourceFieldsRequest,
    ) -> main_models.DescribeDataSourceFieldsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_source_fields_with_options_async(request, runtime)

    def describe_data_source_page_list_with_options(
        self,
        request: main_models.DescribeDataSourcePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourcePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourcePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourcePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_source_page_list_with_options_async(
        self,
        request: main_models.DescribeDataSourcePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourcePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourcePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourcePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_source_page_list(
        self,
        request: main_models.DescribeDataSourcePageListRequest,
    ) -> main_models.DescribeDataSourcePageListResponse:
        runtime = RuntimeOptions()
        return self.describe_data_source_page_list_with_options(request, runtime)

    async def describe_data_source_page_list_async(
        self,
        request: main_models.DescribeDataSourcePageListRequest,
    ) -> main_models.DescribeDataSourcePageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_source_page_list_with_options_async(request, runtime)

    def describe_decision_result_fluctuation_with_options(
        self,
        request: main_models.DescribeDecisionResultFluctuationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDecisionResultFluctuationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDecisionResultFluctuation',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDecisionResultFluctuationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_decision_result_fluctuation_with_options_async(
        self,
        request: main_models.DescribeDecisionResultFluctuationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDecisionResultFluctuationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDecisionResultFluctuation',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDecisionResultFluctuationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_decision_result_fluctuation(
        self,
        request: main_models.DescribeDecisionResultFluctuationRequest,
    ) -> main_models.DescribeDecisionResultFluctuationResponse:
        runtime = RuntimeOptions()
        return self.describe_decision_result_fluctuation_with_options(request, runtime)

    async def describe_decision_result_fluctuation_async(
        self,
        request: main_models.DescribeDecisionResultFluctuationRequest,
    ) -> main_models.DescribeDecisionResultFluctuationResponse:
        runtime = RuntimeOptions()
        return await self.describe_decision_result_fluctuation_with_options_async(request, runtime)

    def describe_decision_result_trend_with_options(
        self,
        request: main_models.DescribeDecisionResultTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDecisionResultTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDecisionResultTrend',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDecisionResultTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_decision_result_trend_with_options_async(
        self,
        request: main_models.DescribeDecisionResultTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDecisionResultTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDecisionResultTrend',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDecisionResultTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_decision_result_trend(
        self,
        request: main_models.DescribeDecisionResultTrendRequest,
    ) -> main_models.DescribeDecisionResultTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_decision_result_trend_with_options(request, runtime)

    async def describe_decision_result_trend_async(
        self,
        request: main_models.DescribeDecisionResultTrendRequest,
    ) -> main_models.DescribeDecisionResultTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_decision_result_trend_with_options_async(request, runtime)

    def describe_detail_start_with_options(
        self,
        request: main_models.DescribeDetailStartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDetailStartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['appKey'] = request.app_key
        if not DaraCore.is_null(request.end_ds):
            query['endDs'] = request.end_ds
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.service):
            query['service'] = request.service
        if not DaraCore.is_null(request.start_ds):
            query['startDs'] = request.start_ds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDetailStart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDetailStartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_detail_start_with_options_async(
        self,
        request: main_models.DescribeDetailStartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDetailStartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['appKey'] = request.app_key
        if not DaraCore.is_null(request.end_ds):
            query['endDs'] = request.end_ds
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.service):
            query['service'] = request.service
        if not DaraCore.is_null(request.start_ds):
            query['startDs'] = request.start_ds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDetailStart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDetailStartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_detail_start(
        self,
        request: main_models.DescribeDetailStartRequest,
    ) -> main_models.DescribeDetailStartResponse:
        runtime = RuntimeOptions()
        return self.describe_detail_start_with_options(request, runtime)

    async def describe_detail_start_async(
        self,
        request: main_models.DescribeDetailStartRequest,
    ) -> main_models.DescribeDetailStartResponse:
        runtime = RuntimeOptions()
        return await self.describe_detail_start_with_options_async(request, runtime)

    def describe_download_url_with_options(
        self,
        request: main_models.DescribeDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_url_with_options_async(
        self,
        request: main_models.DescribeDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_url(
        self,
        request: main_models.DescribeDownloadUrlRequest,
    ) -> main_models.DescribeDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_download_url_with_options(request, runtime)

    async def describe_download_url_async(
        self,
        request: main_models.DescribeDownloadUrlRequest,
    ) -> main_models.DescribeDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_url_with_options_async(request, runtime)

    def describe_event_base_info_by_event_code_with_options(
        self,
        request: main_models.DescribeEventBaseInfoByEventCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventBaseInfoByEventCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventBaseInfoByEventCode',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventBaseInfoByEventCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_base_info_by_event_code_with_options_async(
        self,
        request: main_models.DescribeEventBaseInfoByEventCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventBaseInfoByEventCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventBaseInfoByEventCode',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventBaseInfoByEventCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_base_info_by_event_code(
        self,
        request: main_models.DescribeEventBaseInfoByEventCodeRequest,
    ) -> main_models.DescribeEventBaseInfoByEventCodeResponse:
        runtime = RuntimeOptions()
        return self.describe_event_base_info_by_event_code_with_options(request, runtime)

    async def describe_event_base_info_by_event_code_async(
        self,
        request: main_models.DescribeEventBaseInfoByEventCodeRequest,
    ) -> main_models.DescribeEventBaseInfoByEventCodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_base_info_by_event_code_with_options_async(request, runtime)

    def describe_event_count_with_options(
        self,
        request: main_models.DescribeEventCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventCount',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_count_with_options_async(
        self,
        request: main_models.DescribeEventCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventCount',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_count(
        self,
        request: main_models.DescribeEventCountRequest,
    ) -> main_models.DescribeEventCountResponse:
        runtime = RuntimeOptions()
        return self.describe_event_count_with_options(request, runtime)

    async def describe_event_count_async(
        self,
        request: main_models.DescribeEventCountRequest,
    ) -> main_models.DescribeEventCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_count_with_options_async(request, runtime)

    def describe_event_detail_by_request_id_with_options(
        self,
        request: main_models.DescribeEventDetailByRequestIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventDetailByRequestIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_time):
            query['eventTime'] = request.event_time
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventDetailByRequestId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventDetailByRequestIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_detail_by_request_id_with_options_async(
        self,
        request: main_models.DescribeEventDetailByRequestIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventDetailByRequestIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_time):
            query['eventTime'] = request.event_time
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventDetailByRequestId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventDetailByRequestIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_detail_by_request_id(
        self,
        request: main_models.DescribeEventDetailByRequestIdRequest,
    ) -> main_models.DescribeEventDetailByRequestIdResponse:
        runtime = RuntimeOptions()
        return self.describe_event_detail_by_request_id_with_options(request, runtime)

    async def describe_event_detail_by_request_id_async(
        self,
        request: main_models.DescribeEventDetailByRequestIdRequest,
    ) -> main_models.DescribeEventDetailByRequestIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_detail_by_request_id_with_options_async(request, runtime)

    def describe_event_log_detail_with_options(
        self,
        request: main_models.DescribeEventLogDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventLogDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.req_id_by_log):
            query['reqIdByLog'] = request.req_id_by_log
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventLogDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventLogDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_log_detail_with_options_async(
        self,
        request: main_models.DescribeEventLogDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventLogDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.req_id_by_log):
            query['reqIdByLog'] = request.req_id_by_log
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventLogDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventLogDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_log_detail(
        self,
        request: main_models.DescribeEventLogDetailRequest,
    ) -> main_models.DescribeEventLogDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_event_log_detail_with_options(request, runtime)

    async def describe_event_log_detail_async(
        self,
        request: main_models.DescribeEventLogDetailRequest,
    ) -> main_models.DescribeEventLogDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_log_detail_with_options_async(request, runtime)

    def describe_event_log_page_with_options(
        self,
        request: main_models.DescribeEventLogPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventLogPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.account_id_prp):
            query['accountIdPRP'] = request.account_id_prp
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.condition_1al):
            query['condition1AL'] = request.condition_1al
        if not DaraCore.is_null(request.condition_2al):
            query['condition2AL'] = request.condition_2al
        if not DaraCore.is_null(request.condition_3al):
            query['condition3AL'] = request.condition_3al
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.device_type_lrp):
            query['deviceTypeLRP'] = request.device_type_lrp
        if not DaraCore.is_null(request.email_prp):
            query['emailPRP'] = request.email_prp
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.fail_reason_lrp):
            query['failReasonLRP'] = request.fail_reason_lrp
        if not DaraCore.is_null(request.ip_prp):
            query['ipPRP'] = request.ip_prp
        if not DaraCore.is_null(request.login_result_arp):
            query['loginResultARP'] = request.login_result_arp
        if not DaraCore.is_null(request.login_type_lrp):
            query['loginTypeLRP'] = request.login_type_lrp
        if not DaraCore.is_null(request.mac_prp):
            query['macPRP'] = request.mac_prp
        if not DaraCore.is_null(request.mobile_prp):
            query['mobilePRP'] = request.mobile_prp
        if not DaraCore.is_null(request.nick_name_prp):
            query['nickNamePRP'] = request.nick_name_prp
        if not DaraCore.is_null(request.operate_source_lrp):
            query['operateSourceLRP'] = request.operate_source_lrp
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.refer_prp):
            query['referPRP'] = request.refer_prp
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.register_ip_prp):
            query['registerIpPRP'] = request.register_ip_prp
        if not DaraCore.is_null(request.req_id_pbs):
            query['reqIdPBS'] = request.req_id_pbs
        if not DaraCore.is_null(request.score_ebs):
            query['scoreEBS'] = request.score_ebs
        if not DaraCore.is_null(request.score_sbs):
            query['scoreSBS'] = request.score_sbs
        if not DaraCore.is_null(request.service_abs):
            query['serviceABS'] = request.service_abs
        if not DaraCore.is_null(request.tags_lbs):
            query['tagsLBS'] = request.tags_lbs
        if not DaraCore.is_null(request.umid_pdi):
            query['umidPDI'] = request.umid_pdi
        if not DaraCore.is_null(request.user_agent_prp):
            query['userAgentPRP'] = request.user_agent_prp
        if not DaraCore.is_null(request.user_name_type_lrp):
            query['userNameTypeLRP'] = request.user_name_type_lrp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventLogPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventLogPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_log_page_with_options_async(
        self,
        request: main_models.DescribeEventLogPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventLogPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.account_id_prp):
            query['accountIdPRP'] = request.account_id_prp
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.condition_1al):
            query['condition1AL'] = request.condition_1al
        if not DaraCore.is_null(request.condition_2al):
            query['condition2AL'] = request.condition_2al
        if not DaraCore.is_null(request.condition_3al):
            query['condition3AL'] = request.condition_3al
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.device_type_lrp):
            query['deviceTypeLRP'] = request.device_type_lrp
        if not DaraCore.is_null(request.email_prp):
            query['emailPRP'] = request.email_prp
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.fail_reason_lrp):
            query['failReasonLRP'] = request.fail_reason_lrp
        if not DaraCore.is_null(request.ip_prp):
            query['ipPRP'] = request.ip_prp
        if not DaraCore.is_null(request.login_result_arp):
            query['loginResultARP'] = request.login_result_arp
        if not DaraCore.is_null(request.login_type_lrp):
            query['loginTypeLRP'] = request.login_type_lrp
        if not DaraCore.is_null(request.mac_prp):
            query['macPRP'] = request.mac_prp
        if not DaraCore.is_null(request.mobile_prp):
            query['mobilePRP'] = request.mobile_prp
        if not DaraCore.is_null(request.nick_name_prp):
            query['nickNamePRP'] = request.nick_name_prp
        if not DaraCore.is_null(request.operate_source_lrp):
            query['operateSourceLRP'] = request.operate_source_lrp
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.refer_prp):
            query['referPRP'] = request.refer_prp
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.register_ip_prp):
            query['registerIpPRP'] = request.register_ip_prp
        if not DaraCore.is_null(request.req_id_pbs):
            query['reqIdPBS'] = request.req_id_pbs
        if not DaraCore.is_null(request.score_ebs):
            query['scoreEBS'] = request.score_ebs
        if not DaraCore.is_null(request.score_sbs):
            query['scoreSBS'] = request.score_sbs
        if not DaraCore.is_null(request.service_abs):
            query['serviceABS'] = request.service_abs
        if not DaraCore.is_null(request.tags_lbs):
            query['tagsLBS'] = request.tags_lbs
        if not DaraCore.is_null(request.umid_pdi):
            query['umidPDI'] = request.umid_pdi
        if not DaraCore.is_null(request.user_agent_prp):
            query['userAgentPRP'] = request.user_agent_prp
        if not DaraCore.is_null(request.user_name_type_lrp):
            query['userNameTypeLRP'] = request.user_name_type_lrp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventLogPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventLogPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_log_page(
        self,
        request: main_models.DescribeEventLogPageRequest,
    ) -> main_models.DescribeEventLogPageResponse:
        runtime = RuntimeOptions()
        return self.describe_event_log_page_with_options(request, runtime)

    async def describe_event_log_page_async(
        self,
        request: main_models.DescribeEventLogPageRequest,
    ) -> main_models.DescribeEventLogPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_log_page_with_options_async(request, runtime)

    def describe_event_page_list_with_options(
        self,
        request: main_models.DescribeEventPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.event_status):
            query['eventStatus'] = request.event_status
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_page_list_with_options_async(
        self,
        request: main_models.DescribeEventPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.event_status):
            query['eventStatus'] = request.event_status
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_page_list(
        self,
        request: main_models.DescribeEventPageListRequest,
    ) -> main_models.DescribeEventPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_event_page_list_with_options(request, runtime)

    async def describe_event_page_list_async(
        self,
        request: main_models.DescribeEventPageListRequest,
    ) -> main_models.DescribeEventPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_page_list_with_options_async(request, runtime)

    def describe_event_result_bar_chart_with_options(
        self,
        request: main_models.DescribeEventResultBarChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventResultBarChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventResultBarChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventResultBarChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_result_bar_chart_with_options_async(
        self,
        request: main_models.DescribeEventResultBarChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventResultBarChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventResultBarChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventResultBarChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_result_bar_chart(
        self,
        request: main_models.DescribeEventResultBarChartRequest,
    ) -> main_models.DescribeEventResultBarChartResponse:
        runtime = RuntimeOptions()
        return self.describe_event_result_bar_chart_with_options(request, runtime)

    async def describe_event_result_bar_chart_async(
        self,
        request: main_models.DescribeEventResultBarChartRequest,
    ) -> main_models.DescribeEventResultBarChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_result_bar_chart_with_options_async(request, runtime)

    def describe_event_result_list_with_options(
        self,
        request: main_models.DescribeEventResultListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventResultListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventResultList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventResultListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_result_list_with_options_async(
        self,
        request: main_models.DescribeEventResultListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventResultListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventResultList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventResultListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_result_list(
        self,
        request: main_models.DescribeEventResultListRequest,
    ) -> main_models.DescribeEventResultListResponse:
        runtime = RuntimeOptions()
        return self.describe_event_result_list_with_options(request, runtime)

    async def describe_event_result_list_async(
        self,
        request: main_models.DescribeEventResultListRequest,
    ) -> main_models.DescribeEventResultListResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_result_list_with_options_async(request, runtime)

    def describe_event_task_history_with_options(
        self,
        request: main_models.DescribeEventTaskHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventTaskHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventTaskHistory',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventTaskHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_task_history_with_options_async(
        self,
        request: main_models.DescribeEventTaskHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventTaskHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventTaskHistory',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventTaskHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_task_history(
        self,
        request: main_models.DescribeEventTaskHistoryRequest,
    ) -> main_models.DescribeEventTaskHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_event_task_history_with_options(request, runtime)

    async def describe_event_task_history_async(
        self,
        request: main_models.DescribeEventTaskHistoryRequest,
    ) -> main_models.DescribeEventTaskHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_task_history_with_options_async(request, runtime)

    def describe_event_total_count_report_with_options(
        self,
        request: main_models.DescribeEventTotalCountReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventTotalCountReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventTotalCountReport',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventTotalCountReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_total_count_report_with_options_async(
        self,
        request: main_models.DescribeEventTotalCountReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventTotalCountReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventTotalCountReport',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventTotalCountReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_total_count_report(
        self,
        request: main_models.DescribeEventTotalCountReportRequest,
    ) -> main_models.DescribeEventTotalCountReportResponse:
        runtime = RuntimeOptions()
        return self.describe_event_total_count_report_with_options(request, runtime)

    async def describe_event_total_count_report_async(
        self,
        request: main_models.DescribeEventTotalCountReportRequest,
    ) -> main_models.DescribeEventTotalCountReportResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_total_count_report_with_options_async(request, runtime)

    def describe_event_upload_policy_with_options(
        self,
        request: main_models.DescribeEventUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventUploadPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_upload_policy_with_options_async(
        self,
        request: main_models.DescribeEventUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventUploadPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_upload_policy(
        self,
        request: main_models.DescribeEventUploadPolicyRequest,
    ) -> main_models.DescribeEventUploadPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_event_upload_policy_with_options(request, runtime)

    async def describe_event_upload_policy_async(
        self,
        request: main_models.DescribeEventUploadPolicyRequest,
    ) -> main_models.DescribeEventUploadPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_upload_policy_with_options_async(request, runtime)

    def describe_event_variable_list_with_options(
        self,
        request: main_models.DescribeEventVariableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventVariableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.filter_dto):
            query['filterDTO'] = request.filter_dto
        if not DaraCore.is_null(request.ref_obj_id):
            query['refObjId'] = request.ref_obj_id
        if not DaraCore.is_null(request.ref_obj_type):
            query['refObjType'] = request.ref_obj_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventVariableList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventVariableListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_variable_list_with_options_async(
        self,
        request: main_models.DescribeEventVariableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventVariableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.filter_dto):
            query['filterDTO'] = request.filter_dto
        if not DaraCore.is_null(request.ref_obj_id):
            query['refObjId'] = request.ref_obj_id
        if not DaraCore.is_null(request.ref_obj_type):
            query['refObjType'] = request.ref_obj_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventVariableList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventVariableListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_variable_list(
        self,
        request: main_models.DescribeEventVariableListRequest,
    ) -> main_models.DescribeEventVariableListResponse:
        runtime = RuntimeOptions()
        return self.describe_event_variable_list_with_options(request, runtime)

    async def describe_event_variable_list_async(
        self,
        request: main_models.DescribeEventVariableListRequest,
    ) -> main_models.DescribeEventVariableListResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_variable_list_with_options_async(request, runtime)

    def describe_event_variable_template_bind_with_options(
        self,
        request: main_models.DescribeEventVariableTemplateBindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventVariableTemplateBindResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.inputs):
            query['inputs'] = request.inputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_code):
            query['templateCode'] = request.template_code
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventVariableTemplateBind',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventVariableTemplateBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_variable_template_bind_with_options_async(
        self,
        request: main_models.DescribeEventVariableTemplateBindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventVariableTemplateBindResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.inputs):
            query['inputs'] = request.inputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_code):
            query['templateCode'] = request.template_code
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventVariableTemplateBind',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventVariableTemplateBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_variable_template_bind(
        self,
        request: main_models.DescribeEventVariableTemplateBindRequest,
    ) -> main_models.DescribeEventVariableTemplateBindResponse:
        runtime = RuntimeOptions()
        return self.describe_event_variable_template_bind_with_options(request, runtime)

    async def describe_event_variable_template_bind_async(
        self,
        request: main_models.DescribeEventVariableTemplateBindRequest,
    ) -> main_models.DescribeEventVariableTemplateBindResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_variable_template_bind_with_options_async(request, runtime)

    def describe_event_variable_template_list_with_options(
        self,
        request: main_models.DescribeEventVariableTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventVariableTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.inputs):
            query['inputs'] = request.inputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_code):
            query['templateCode'] = request.template_code
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventVariableTemplateList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventVariableTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_variable_template_list_with_options_async(
        self,
        request: main_models.DescribeEventVariableTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventVariableTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.inputs):
            query['inputs'] = request.inputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_code):
            query['templateCode'] = request.template_code
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventVariableTemplateList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventVariableTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_variable_template_list(
        self,
        request: main_models.DescribeEventVariableTemplateListRequest,
    ) -> main_models.DescribeEventVariableTemplateListResponse:
        runtime = RuntimeOptions()
        return self.describe_event_variable_template_list_with_options(request, runtime)

    async def describe_event_variable_template_list_async(
        self,
        request: main_models.DescribeEventVariableTemplateListRequest,
    ) -> main_models.DescribeEventVariableTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_variable_template_list_with_options_async(request, runtime)

    def describe_events_variable_list_with_options(
        self,
        request: main_models.DescribeEventsVariableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsVariableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.filter_dto):
            query['filterDTO'] = request.filter_dto
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventsVariableList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsVariableListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_variable_list_with_options_async(
        self,
        request: main_models.DescribeEventsVariableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsVariableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.filter_dto):
            query['filterDTO'] = request.filter_dto
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventsVariableList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsVariableListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events_variable_list(
        self,
        request: main_models.DescribeEventsVariableListRequest,
    ) -> main_models.DescribeEventsVariableListResponse:
        runtime = RuntimeOptions()
        return self.describe_events_variable_list_with_options(request, runtime)

    async def describe_events_variable_list_async(
        self,
        request: main_models.DescribeEventsVariableListRequest,
    ) -> main_models.DescribeEventsVariableListResponse:
        runtime = RuntimeOptions()
        return await self.describe_events_variable_list_with_options_async(request, runtime)

    def describe_excute_num_with_options(
        self,
        request: main_models.DescribeExcuteNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExcuteNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.degree):
            query['Degree'] = request.degree
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExcuteNum',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExcuteNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_excute_num_with_options_async(
        self,
        request: main_models.DescribeExcuteNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExcuteNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.degree):
            query['Degree'] = request.degree
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExcuteNum',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExcuteNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_excute_num(
        self,
        request: main_models.DescribeExcuteNumRequest,
    ) -> main_models.DescribeExcuteNumResponse:
        runtime = RuntimeOptions()
        return self.describe_excute_num_with_options(request, runtime)

    async def describe_excute_num_async(
        self,
        request: main_models.DescribeExcuteNumRequest,
    ) -> main_models.DescribeExcuteNumResponse:
        runtime = RuntimeOptions()
        return await self.describe_excute_num_with_options_async(request, runtime)

    def describe_exist_name_with_options(
        self,
        request: main_models.DescribeExistNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExistNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExistName',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExistNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exist_name_with_options_async(
        self,
        request: main_models.DescribeExistNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExistNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExistName',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExistNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exist_name(
        self,
        request: main_models.DescribeExistNameRequest,
    ) -> main_models.DescribeExistNameResponse:
        runtime = RuntimeOptions()
        return self.describe_exist_name_with_options(request, runtime)

    async def describe_exist_name_async(
        self,
        request: main_models.DescribeExistNameRequest,
    ) -> main_models.DescribeExistNameResponse:
        runtime = RuntimeOptions()
        return await self.describe_exist_name_with_options_async(request, runtime)

    def describe_exist_scene_with_options(
        self,
        request: main_models.DescribeExistSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExistSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExistScene',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExistSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exist_scene_with_options_async(
        self,
        request: main_models.DescribeExistSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExistSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExistScene',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExistSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exist_scene(
        self,
        request: main_models.DescribeExistSceneRequest,
    ) -> main_models.DescribeExistSceneResponse:
        runtime = RuntimeOptions()
        return self.describe_exist_scene_with_options(request, runtime)

    async def describe_exist_scene_async(
        self,
        request: main_models.DescribeExistSceneRequest,
    ) -> main_models.DescribeExistSceneResponse:
        runtime = RuntimeOptions()
        return await self.describe_exist_scene_with_options_async(request, runtime)

    def describe_expression_variable_detail_with_options(
        self,
        request: main_models.DescribeExpressionVariableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressionVariableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressionVariableDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressionVariableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_expression_variable_detail_with_options_async(
        self,
        request: main_models.DescribeExpressionVariableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressionVariableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressionVariableDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressionVariableDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_expression_variable_detail(
        self,
        request: main_models.DescribeExpressionVariableDetailRequest,
    ) -> main_models.DescribeExpressionVariableDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_expression_variable_detail_with_options(request, runtime)

    async def describe_expression_variable_detail_async(
        self,
        request: main_models.DescribeExpressionVariableDetailRequest,
    ) -> main_models.DescribeExpressionVariableDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_expression_variable_detail_with_options_async(request, runtime)

    def describe_expression_variable_function_list_with_options(
        self,
        request: main_models.DescribeExpressionVariableFunctionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressionVariableFunctionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressionVariableFunctionList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressionVariableFunctionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_expression_variable_function_list_with_options_async(
        self,
        request: main_models.DescribeExpressionVariableFunctionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressionVariableFunctionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressionVariableFunctionList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressionVariableFunctionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_expression_variable_function_list(
        self,
        request: main_models.DescribeExpressionVariableFunctionListRequest,
    ) -> main_models.DescribeExpressionVariableFunctionListResponse:
        runtime = RuntimeOptions()
        return self.describe_expression_variable_function_list_with_options(request, runtime)

    async def describe_expression_variable_function_list_async(
        self,
        request: main_models.DescribeExpressionVariableFunctionListRequest,
    ) -> main_models.DescribeExpressionVariableFunctionListResponse:
        runtime = RuntimeOptions()
        return await self.describe_expression_variable_function_list_with_options_async(request, runtime)

    def describe_expression_variable_page_with_options(
        self,
        request: main_models.DescribeExpressionVariablePageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressionVariablePageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressionVariablePage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressionVariablePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_expression_variable_page_with_options_async(
        self,
        request: main_models.DescribeExpressionVariablePageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressionVariablePageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressionVariablePage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressionVariablePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_expression_variable_page(
        self,
        request: main_models.DescribeExpressionVariablePageRequest,
    ) -> main_models.DescribeExpressionVariablePageResponse:
        runtime = RuntimeOptions()
        return self.describe_expression_variable_page_with_options(request, runtime)

    async def describe_expression_variable_page_async(
        self,
        request: main_models.DescribeExpressionVariablePageRequest,
    ) -> main_models.DescribeExpressionVariablePageResponse:
        runtime = RuntimeOptions()
        return await self.describe_expression_variable_page_with_options_async(request, runtime)

    def describe_expression_variable_version_detail_with_options(
        self,
        request: main_models.DescribeExpressionVariableVersionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressionVariableVersionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_code):
            query['objectCode'] = request.object_code
        if not DaraCore.is_null(request.object_id):
            query['objectId'] = request.object_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressionVariableVersionDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressionVariableVersionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_expression_variable_version_detail_with_options_async(
        self,
        request: main_models.DescribeExpressionVariableVersionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressionVariableVersionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_code):
            query['objectCode'] = request.object_code
        if not DaraCore.is_null(request.object_id):
            query['objectId'] = request.object_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressionVariableVersionDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressionVariableVersionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_expression_variable_version_detail(
        self,
        request: main_models.DescribeExpressionVariableVersionDetailRequest,
    ) -> main_models.DescribeExpressionVariableVersionDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_expression_variable_version_detail_with_options(request, runtime)

    async def describe_expression_variable_version_detail_async(
        self,
        request: main_models.DescribeExpressionVariableVersionDetailRequest,
    ) -> main_models.DescribeExpressionVariableVersionDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_expression_variable_version_detail_with_options_async(request, runtime)

    def describe_field_by_id_with_options(
        self,
        request: main_models.DescribeFieldByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFieldByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFieldById',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFieldByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_field_by_id_with_options_async(
        self,
        request: main_models.DescribeFieldByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFieldByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFieldById',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFieldByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_field_by_id(
        self,
        request: main_models.DescribeFieldByIdRequest,
    ) -> main_models.DescribeFieldByIdResponse:
        runtime = RuntimeOptions()
        return self.describe_field_by_id_with_options(request, runtime)

    async def describe_field_by_id_async(
        self,
        request: main_models.DescribeFieldByIdRequest,
    ) -> main_models.DescribeFieldByIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_field_by_id_with_options_async(request, runtime)

    def describe_field_list_with_options(
        self,
        request: main_models.DescribeFieldListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFieldListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.inputs):
            query['inputs'] = request.inputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFieldList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFieldListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_field_list_with_options_async(
        self,
        request: main_models.DescribeFieldListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFieldListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.inputs):
            query['inputs'] = request.inputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFieldList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFieldListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_field_list(
        self,
        request: main_models.DescribeFieldListRequest,
    ) -> main_models.DescribeFieldListResponse:
        runtime = RuntimeOptions()
        return self.describe_field_list_with_options(request, runtime)

    async def describe_field_list_async(
        self,
        request: main_models.DescribeFieldListRequest,
    ) -> main_models.DescribeFieldListResponse:
        runtime = RuntimeOptions()
        return await self.describe_field_list_with_options_async(request, runtime)

    def describe_field_page_with_options(
        self,
        request: main_models.DescribeFieldPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFieldPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.classify):
            query['classify'] = request.classify
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFieldPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFieldPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_field_page_with_options_async(
        self,
        request: main_models.DescribeFieldPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFieldPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.classify):
            query['classify'] = request.classify
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFieldPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFieldPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_field_page(
        self,
        request: main_models.DescribeFieldPageRequest,
    ) -> main_models.DescribeFieldPageResponse:
        runtime = RuntimeOptions()
        return self.describe_field_page_with_options(request, runtime)

    async def describe_field_page_async(
        self,
        request: main_models.DescribeFieldPageRequest,
    ) -> main_models.DescribeFieldPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_field_page_with_options_async(request, runtime)

    def describe_group_account_page_with_options(
        self,
        request: main_models.DescribeGroupAccountPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupAccountPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.community_no):
            query['communityNo'] = request.community_no
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.field_key):
            query['fieldKey'] = request.field_key
        if not DaraCore.is_null(request.field_val):
            query['fieldVal'] = request.field_val
        if not DaraCore.is_null(request.is_page):
            query['isPage'] = request.is_page
        if not DaraCore.is_null(request.order):
            query['order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupAccountPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupAccountPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_account_page_with_options_async(
        self,
        request: main_models.DescribeGroupAccountPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupAccountPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.community_no):
            query['communityNo'] = request.community_no
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.field_key):
            query['fieldKey'] = request.field_key
        if not DaraCore.is_null(request.field_val):
            query['fieldVal'] = request.field_val
        if not DaraCore.is_null(request.is_page):
            query['isPage'] = request.is_page
        if not DaraCore.is_null(request.order):
            query['order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupAccountPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupAccountPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_account_page(
        self,
        request: main_models.DescribeGroupAccountPageRequest,
    ) -> main_models.DescribeGroupAccountPageResponse:
        runtime = RuntimeOptions()
        return self.describe_group_account_page_with_options(request, runtime)

    async def describe_group_account_page_async(
        self,
        request: main_models.DescribeGroupAccountPageRequest,
    ) -> main_models.DescribeGroupAccountPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_account_page_with_options_async(request, runtime)

    def describe_group_condition_list_with_options(
        self,
        request: main_models.DescribeGroupConditionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupConditionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupConditionList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupConditionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_condition_list_with_options_async(
        self,
        request: main_models.DescribeGroupConditionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupConditionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupConditionList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupConditionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_condition_list(
        self,
        request: main_models.DescribeGroupConditionListRequest,
    ) -> main_models.DescribeGroupConditionListResponse:
        runtime = RuntimeOptions()
        return self.describe_group_condition_list_with_options(request, runtime)

    async def describe_group_condition_list_async(
        self,
        request: main_models.DescribeGroupConditionListRequest,
    ) -> main_models.DescribeGroupConditionListResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_condition_list_with_options_async(request, runtime)

    def describe_group_page_with_options(
        self,
        request: main_models.DescribeGroupPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.order):
            query['order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        if not DaraCore.is_null(request.time_type):
            query['timeType'] = request.time_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_page_with_options_async(
        self,
        request: main_models.DescribeGroupPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.order):
            query['order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        if not DaraCore.is_null(request.time_type):
            query['timeType'] = request.time_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_page(
        self,
        request: main_models.DescribeGroupPageRequest,
    ) -> main_models.DescribeGroupPageResponse:
        runtime = RuntimeOptions()
        return self.describe_group_page_with_options(request, runtime)

    async def describe_group_page_async(
        self,
        request: main_models.DescribeGroupPageRequest,
    ) -> main_models.DescribeGroupPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_page_with_options_async(request, runtime)

    def describe_group_statistics_by_today_with_options(
        self,
        request: main_models.DescribeGroupStatisticsByTodayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupStatisticsByTodayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupStatisticsByToday',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupStatisticsByTodayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_statistics_by_today_with_options_async(
        self,
        request: main_models.DescribeGroupStatisticsByTodayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupStatisticsByTodayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupStatisticsByToday',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupStatisticsByTodayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_statistics_by_today(
        self,
        request: main_models.DescribeGroupStatisticsByTodayRequest,
    ) -> main_models.DescribeGroupStatisticsByTodayResponse:
        runtime = RuntimeOptions()
        return self.describe_group_statistics_by_today_with_options(request, runtime)

    async def describe_group_statistics_by_today_async(
        self,
        request: main_models.DescribeGroupStatisticsByTodayRequest,
    ) -> main_models.DescribeGroupStatisticsByTodayResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_statistics_by_today_with_options_async(request, runtime)

    def describe_group_trend_with_options(
        self,
        request: main_models.DescribeGroupTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.day):
            query['day'] = request.day
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupTrend',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_trend_with_options_async(
        self,
        request: main_models.DescribeGroupTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.day):
            query['day'] = request.day
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupTrend',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_trend(
        self,
        request: main_models.DescribeGroupTrendRequest,
    ) -> main_models.DescribeGroupTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_group_trend_with_options(request, runtime)

    async def describe_group_trend_async(
        self,
        request: main_models.DescribeGroupTrendRequest,
    ) -> main_models.DescribeGroupTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_trend_with_options_async(request, runtime)

    def describe_has_rule_name_by_event_code_with_options(
        self,
        request: main_models.DescribeHasRuleNameByEventCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHasRuleNameByEventCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.exclude_rule_id):
            query['excludeRuleId'] = request.exclude_rule_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHasRuleNameByEventCode',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHasRuleNameByEventCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_has_rule_name_by_event_code_with_options_async(
        self,
        request: main_models.DescribeHasRuleNameByEventCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHasRuleNameByEventCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.exclude_rule_id):
            query['excludeRuleId'] = request.exclude_rule_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHasRuleNameByEventCode',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHasRuleNameByEventCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_has_rule_name_by_event_code(
        self,
        request: main_models.DescribeHasRuleNameByEventCodeRequest,
    ) -> main_models.DescribeHasRuleNameByEventCodeResponse:
        runtime = RuntimeOptions()
        return self.describe_has_rule_name_by_event_code_with_options(request, runtime)

    async def describe_has_rule_name_by_event_code_async(
        self,
        request: main_models.DescribeHasRuleNameByEventCodeRequest,
    ) -> main_models.DescribeHasRuleNameByEventCodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_has_rule_name_by_event_code_with_options_async(request, runtime)

    def describe_high_risk_pie_chart_with_options(
        self,
        request: main_models.DescribeHighRiskPieChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHighRiskPieChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHighRiskPieChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHighRiskPieChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_high_risk_pie_chart_with_options_async(
        self,
        request: main_models.DescribeHighRiskPieChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHighRiskPieChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHighRiskPieChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHighRiskPieChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_high_risk_pie_chart(
        self,
        request: main_models.DescribeHighRiskPieChartRequest,
    ) -> main_models.DescribeHighRiskPieChartResponse:
        runtime = RuntimeOptions()
        return self.describe_high_risk_pie_chart_with_options(request, runtime)

    async def describe_high_risk_pie_chart_async(
        self,
        request: main_models.DescribeHighRiskPieChartRequest,
    ) -> main_models.DescribeHighRiskPieChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_high_risk_pie_chart_with_options_async(request, runtime)

    def describe_hit_rule_fluctuation_with_options(
        self,
        request: main_models.DescribeHitRuleFluctuationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHitRuleFluctuationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHitRuleFluctuation',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHitRuleFluctuationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hit_rule_fluctuation_with_options_async(
        self,
        request: main_models.DescribeHitRuleFluctuationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHitRuleFluctuationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHitRuleFluctuation',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHitRuleFluctuationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hit_rule_fluctuation(
        self,
        request: main_models.DescribeHitRuleFluctuationRequest,
    ) -> main_models.DescribeHitRuleFluctuationResponse:
        runtime = RuntimeOptions()
        return self.describe_hit_rule_fluctuation_with_options(request, runtime)

    async def describe_hit_rule_fluctuation_async(
        self,
        request: main_models.DescribeHitRuleFluctuationRequest,
    ) -> main_models.DescribeHitRuleFluctuationResponse:
        runtime = RuntimeOptions()
        return await self.describe_hit_rule_fluctuation_with_options_async(request, runtime)

    def describe_hit_rule_list_with_options(
        self,
        request: main_models.DescribeHitRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHitRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_type):
            query['eventType'] = request.event_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHitRuleList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHitRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hit_rule_list_with_options_async(
        self,
        request: main_models.DescribeHitRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHitRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_type):
            query['eventType'] = request.event_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHitRuleList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHitRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hit_rule_list(
        self,
        request: main_models.DescribeHitRuleListRequest,
    ) -> main_models.DescribeHitRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_hit_rule_list_with_options(request, runtime)

    async def describe_hit_rule_list_async(
        self,
        request: main_models.DescribeHitRuleListRequest,
    ) -> main_models.DescribeHitRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_hit_rule_list_with_options_async(request, runtime)

    def describe_hit_rule_trend_with_options(
        self,
        request: main_models.DescribeHitRuleTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHitRuleTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHitRuleTrend',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHitRuleTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hit_rule_trend_with_options_async(
        self,
        request: main_models.DescribeHitRuleTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHitRuleTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHitRuleTrend',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHitRuleTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hit_rule_trend(
        self,
        request: main_models.DescribeHitRuleTrendRequest,
    ) -> main_models.DescribeHitRuleTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_hit_rule_trend_with_options(request, runtime)

    async def describe_hit_rule_trend_async(
        self,
        request: main_models.DescribeHitRuleTrendRequest,
    ) -> main_models.DescribeHitRuleTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_hit_rule_trend_with_options_async(request, runtime)

    def describe_init_dig_with_options(
        self,
        request: main_models.DescribeInitDigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInitDigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInitDig',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInitDigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_init_dig_with_options_async(
        self,
        request: main_models.DescribeInitDigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInitDigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInitDig',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInitDigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_init_dig(
        self,
        request: main_models.DescribeInitDigRequest,
    ) -> main_models.DescribeInitDigResponse:
        runtime = RuntimeOptions()
        return self.describe_init_dig_with_options(request, runtime)

    async def describe_init_dig_async(
        self,
        request: main_models.DescribeInitDigRequest,
    ) -> main_models.DescribeInitDigResponse:
        runtime = RuntimeOptions()
        return await self.describe_init_dig_with_options_async(request, runtime)

    def describe_input_feild_count_by_event_code_with_options(
        self,
        request: main_models.DescribeInputFeildCountByEventCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInputFeildCountByEventCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInputFeildCountByEventCode',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInputFeildCountByEventCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_input_feild_count_by_event_code_with_options_async(
        self,
        request: main_models.DescribeInputFeildCountByEventCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInputFeildCountByEventCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInputFeildCountByEventCode',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInputFeildCountByEventCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_input_feild_count_by_event_code(
        self,
        request: main_models.DescribeInputFeildCountByEventCodeRequest,
    ) -> main_models.DescribeInputFeildCountByEventCodeResponse:
        runtime = RuntimeOptions()
        return self.describe_input_feild_count_by_event_code_with_options(request, runtime)

    async def describe_input_feild_count_by_event_code_async(
        self,
        request: main_models.DescribeInputFeildCountByEventCodeRequest,
    ) -> main_models.DescribeInputFeildCountByEventCodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_input_feild_count_by_event_code_with_options_async(request, runtime)

    def describe_list_model_with_options(
        self,
        request: main_models.DescribeListModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListModel',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_list_model_with_options_async(
        self,
        request: main_models.DescribeListModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListModel',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_list_model(
        self,
        request: main_models.DescribeListModelRequest,
    ) -> main_models.DescribeListModelResponse:
        runtime = RuntimeOptions()
        return self.describe_list_model_with_options(request, runtime)

    async def describe_list_model_async(
        self,
        request: main_models.DescribeListModelRequest,
    ) -> main_models.DescribeListModelResponse:
        runtime = RuntimeOptions()
        return await self.describe_list_model_with_options_async(request, runtime)

    def describe_list_poc_with_options(
        self,
        request: main_models.DescribeListPocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListPocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListPoc',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListPocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_list_poc_with_options_async(
        self,
        request: main_models.DescribeListPocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListPocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListPoc',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListPocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_list_poc(
        self,
        request: main_models.DescribeListPocRequest,
    ) -> main_models.DescribeListPocResponse:
        runtime = RuntimeOptions()
        return self.describe_list_poc_with_options(request, runtime)

    async def describe_list_poc_async(
        self,
        request: main_models.DescribeListPocRequest,
    ) -> main_models.DescribeListPocResponse:
        runtime = RuntimeOptions()
        return await self.describe_list_poc_with_options_async(request, runtime)

    def describe_loan_exec_list_with_options(
        self,
        request: main_models.DescribeLoanExecListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoanExecListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_no):
            query['batchNo'] = request.batch_no
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.monitor_obj):
            query['monitorObj'] = request.monitor_obj
        if not DaraCore.is_null(request.monitor_status):
            query['monitorStatus'] = request.monitor_status
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoanExecList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoanExecListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_loan_exec_list_with_options_async(
        self,
        request: main_models.DescribeLoanExecListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoanExecListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_no):
            query['batchNo'] = request.batch_no
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.monitor_obj):
            query['monitorObj'] = request.monitor_obj
        if not DaraCore.is_null(request.monitor_status):
            query['monitorStatus'] = request.monitor_status
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoanExecList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoanExecListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_loan_exec_list(
        self,
        request: main_models.DescribeLoanExecListRequest,
    ) -> main_models.DescribeLoanExecListResponse:
        runtime = RuntimeOptions()
        return self.describe_loan_exec_list_with_options(request, runtime)

    async def describe_loan_exec_list_async(
        self,
        request: main_models.DescribeLoanExecListRequest,
    ) -> main_models.DescribeLoanExecListResponse:
        runtime = RuntimeOptions()
        return await self.describe_loan_exec_list_with_options_async(request, runtime)

    def describe_loan_task_list_with_options(
        self,
        request: main_models.DescribeLoanTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoanTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_no):
            query['batchNo'] = request.batch_no
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.monitor_status):
            query['monitorStatus'] = request.monitor_status
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoanTaskList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoanTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_loan_task_list_with_options_async(
        self,
        request: main_models.DescribeLoanTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoanTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_no):
            query['batchNo'] = request.batch_no
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.monitor_status):
            query['monitorStatus'] = request.monitor_status
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoanTaskList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoanTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_loan_task_list(
        self,
        request: main_models.DescribeLoanTaskListRequest,
    ) -> main_models.DescribeLoanTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_loan_task_list_with_options(request, runtime)

    async def describe_loan_task_list_async(
        self,
        request: main_models.DescribeLoanTaskListRequest,
    ) -> main_models.DescribeLoanTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_loan_task_list_with_options_async(request, runtime)

    def describe_mark_page_with_options(
        self,
        request: main_models.DescribeMarkPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMarkPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.is_page):
            query['isPage'] = request.is_page
        if not DaraCore.is_null(request.order):
            query['order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_log_id):
            query['taskLogId'] = request.task_log_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMarkPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMarkPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mark_page_with_options_async(
        self,
        request: main_models.DescribeMarkPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMarkPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.is_page):
            query['isPage'] = request.is_page
        if not DaraCore.is_null(request.order):
            query['order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_log_id):
            query['taskLogId'] = request.task_log_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMarkPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMarkPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mark_page(
        self,
        request: main_models.DescribeMarkPageRequest,
    ) -> main_models.DescribeMarkPageResponse:
        runtime = RuntimeOptions()
        return self.describe_mark_page_with_options(request, runtime)

    async def describe_mark_page_async(
        self,
        request: main_models.DescribeMarkPageRequest,
    ) -> main_models.DescribeMarkPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_mark_page_with_options_async(request, runtime)

    def describe_menu_permission_with_options(
        self,
        request: main_models.DescribeMenuPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMenuPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.permission_type):
            query['permissionType'] = request.permission_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMenuPermission',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMenuPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_menu_permission_with_options_async(
        self,
        request: main_models.DescribeMenuPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMenuPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.permission_type):
            query['permissionType'] = request.permission_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMenuPermission',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMenuPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_menu_permission(
        self,
        request: main_models.DescribeMenuPermissionRequest,
    ) -> main_models.DescribeMenuPermissionResponse:
        runtime = RuntimeOptions()
        return self.describe_menu_permission_with_options(request, runtime)

    async def describe_menu_permission_async(
        self,
        request: main_models.DescribeMenuPermissionRequest,
    ) -> main_models.DescribeMenuPermissionResponse:
        runtime = RuntimeOptions()
        return await self.describe_menu_permission_with_options_async(request, runtime)

    def describe_model_details_by_id_with_options(
        self,
        request: main_models.DescribeModelDetailsByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelDetailsByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelDetailsById',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModelDetailsByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_model_details_by_id_with_options_async(
        self,
        request: main_models.DescribeModelDetailsByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelDetailsByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelDetailsById',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModelDetailsByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_model_details_by_id(
        self,
        request: main_models.DescribeModelDetailsByIdRequest,
    ) -> main_models.DescribeModelDetailsByIdResponse:
        runtime = RuntimeOptions()
        return self.describe_model_details_by_id_with_options(request, runtime)

    async def describe_model_details_by_id_async(
        self,
        request: main_models.DescribeModelDetailsByIdRequest,
    ) -> main_models.DescribeModelDetailsByIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_model_details_by_id_with_options_async(request, runtime)

    def describe_model_oss_policy_with_options(
        self,
        request: main_models.DescribeModelOssPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelOssPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelOssPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModelOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_model_oss_policy_with_options_async(
        self,
        request: main_models.DescribeModelOssPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelOssPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelOssPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModelOssPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_model_oss_policy(
        self,
        request: main_models.DescribeModelOssPolicyRequest,
    ) -> main_models.DescribeModelOssPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_model_oss_policy_with_options(request, runtime)

    async def describe_model_oss_policy_async(
        self,
        request: main_models.DescribeModelOssPolicyRequest,
    ) -> main_models.DescribeModelOssPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_model_oss_policy_with_options_async(request, runtime)

    def describe_monitor_task_limit_with_options(
        self,
        request: main_models.DescribeMonitorTaskLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorTaskLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorTaskLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorTaskLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_task_limit_with_options_async(
        self,
        request: main_models.DescribeMonitorTaskLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorTaskLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorTaskLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorTaskLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_task_limit(
        self,
        request: main_models.DescribeMonitorTaskLimitRequest,
    ) -> main_models.DescribeMonitorTaskLimitResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_task_limit_with_options(request, runtime)

    async def describe_monitor_task_limit_async(
        self,
        request: main_models.DescribeMonitorTaskLimitRequest,
    ) -> main_models.DescribeMonitorTaskLimitResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_task_limit_with_options_async(request, runtime)

    def describe_name_list_with_options(
        self,
        request: main_models.DescribeNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_name_list_with_options_async(
        self,
        request: main_models.DescribeNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_name_list(
        self,
        request: main_models.DescribeNameListRequest,
    ) -> main_models.DescribeNameListResponse:
        runtime = RuntimeOptions()
        return self.describe_name_list_with_options(request, runtime)

    async def describe_name_list_async(
        self,
        request: main_models.DescribeNameListRequest,
    ) -> main_models.DescribeNameListResponse:
        runtime = RuntimeOptions()
        return await self.describe_name_list_with_options_async(request, runtime)

    def describe_name_list_download_url_with_options(
        self,
        request: main_models.DescribeNameListDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_name_list_download_url_with_options_async(
        self,
        request: main_models.DescribeNameListDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_name_list_download_url(
        self,
        request: main_models.DescribeNameListDownloadUrlRequest,
    ) -> main_models.DescribeNameListDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_name_list_download_url_with_options(request, runtime)

    async def describe_name_list_download_url_async(
        self,
        request: main_models.DescribeNameListDownloadUrlRequest,
    ) -> main_models.DescribeNameListDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_name_list_download_url_with_options_async(request, runtime)

    def describe_name_list_limit_with_options(
        self,
        request: main_models.DescribeNameListLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_name_list_limit_with_options_async(
        self,
        request: main_models.DescribeNameListLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListLimit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_name_list_limit(
        self,
        request: main_models.DescribeNameListLimitRequest,
    ) -> main_models.DescribeNameListLimitResponse:
        runtime = RuntimeOptions()
        return self.describe_name_list_limit_with_options(request, runtime)

    async def describe_name_list_limit_async(
        self,
        request: main_models.DescribeNameListLimitRequest,
    ) -> main_models.DescribeNameListLimitResponse:
        runtime = RuntimeOptions()
        return await self.describe_name_list_limit_with_options_async(request, runtime)

    def describe_name_list_page_list_with_options(
        self,
        request: main_models.DescribeNameListPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.update_begin_time):
            query['updateBeginTime'] = request.update_begin_time
        if not DaraCore.is_null(request.update_end_time):
            query['updateEndTime'] = request.update_end_time
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_name_list_page_list_with_options_async(
        self,
        request: main_models.DescribeNameListPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.update_begin_time):
            query['updateBeginTime'] = request.update_begin_time
        if not DaraCore.is_null(request.update_end_time):
            query['updateEndTime'] = request.update_end_time
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_name_list_page_list(
        self,
        request: main_models.DescribeNameListPageListRequest,
    ) -> main_models.DescribeNameListPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_name_list_page_list_with_options(request, runtime)

    async def describe_name_list_page_list_async(
        self,
        request: main_models.DescribeNameListPageListRequest,
    ) -> main_models.DescribeNameListPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_name_list_page_list_with_options_async(request, runtime)

    def describe_name_list_type_list_with_options(
        self,
        request: main_models.DescribeNameListTypeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListTypeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListTypeList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_name_list_type_list_with_options_async(
        self,
        request: main_models.DescribeNameListTypeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListTypeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListTypeList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListTypeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_name_list_type_list(
        self,
        request: main_models.DescribeNameListTypeListRequest,
    ) -> main_models.DescribeNameListTypeListResponse:
        runtime = RuntimeOptions()
        return self.describe_name_list_type_list_with_options(request, runtime)

    async def describe_name_list_type_list_async(
        self,
        request: main_models.DescribeNameListTypeListRequest,
    ) -> main_models.DescribeNameListTypeListResponse:
        runtime = RuntimeOptions()
        return await self.describe_name_list_type_list_with_options_async(request, runtime)

    def describe_name_list_variable_page_list_with_options(
        self,
        request: main_models.DescribeNameListVariablePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListVariablePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_list_type):
            query['nameListType'] = request.name_list_type
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListVariablePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListVariablePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_name_list_variable_page_list_with_options_async(
        self,
        request: main_models.DescribeNameListVariablePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNameListVariablePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_list_type):
            query['nameListType'] = request.name_list_type
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNameListVariablePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNameListVariablePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_name_list_variable_page_list(
        self,
        request: main_models.DescribeNameListVariablePageListRequest,
    ) -> main_models.DescribeNameListVariablePageListResponse:
        runtime = RuntimeOptions()
        return self.describe_name_list_variable_page_list_with_options(request, runtime)

    async def describe_name_list_variable_page_list_async(
        self,
        request: main_models.DescribeNameListVariablePageListRequest,
    ) -> main_models.DescribeNameListVariablePageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_name_list_variable_page_list_with_options_async(request, runtime)

    def describe_operation_log_monitoring_with_options(
        self,
        request: main_models.DescribeOperationLogMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperationLogMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        if not DaraCore.is_null(request.user_name_search):
            query['userNameSearch'] = request.user_name_search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperationLogMonitoring',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperationLogMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operation_log_monitoring_with_options_async(
        self,
        request: main_models.DescribeOperationLogMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperationLogMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        if not DaraCore.is_null(request.user_name_search):
            query['userNameSearch'] = request.user_name_search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperationLogMonitoring',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperationLogMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operation_log_monitoring(
        self,
        request: main_models.DescribeOperationLogMonitoringRequest,
    ) -> main_models.DescribeOperationLogMonitoringResponse:
        runtime = RuntimeOptions()
        return self.describe_operation_log_monitoring_with_options(request, runtime)

    async def describe_operation_log_monitoring_async(
        self,
        request: main_models.DescribeOperationLogMonitoringRequest,
    ) -> main_models.DescribeOperationLogMonitoringResponse:
        runtime = RuntimeOptions()
        return await self.describe_operation_log_monitoring_with_options_async(request, runtime)

    def describe_operation_log_page_list_with_options(
        self,
        request: main_models.DescribeOperationLogPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperationLogPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.operation_summary):
            query['operationSummary'] = request.operation_summary
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        if not DaraCore.is_null(request.user_name_search):
            query['userNameSearch'] = request.user_name_search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperationLogPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperationLogPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operation_log_page_list_with_options_async(
        self,
        request: main_models.DescribeOperationLogPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperationLogPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.operation_summary):
            query['operationSummary'] = request.operation_summary
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        if not DaraCore.is_null(request.user_name_search):
            query['userNameSearch'] = request.user_name_search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperationLogPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperationLogPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operation_log_page_list(
        self,
        request: main_models.DescribeOperationLogPageListRequest,
    ) -> main_models.DescribeOperationLogPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_operation_log_page_list_with_options(request, runtime)

    async def describe_operation_log_page_list_async(
        self,
        request: main_models.DescribeOperationLogPageListRequest,
    ) -> main_models.DescribeOperationLogPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_operation_log_page_list_with_options_async(request, runtime)

    def describe_operator_list_with_options(
        self,
        request: main_models.DescribeOperatorListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperatorList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operator_list_with_options_async(
        self,
        request: main_models.DescribeOperatorListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperatorList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operator_list(
        self,
        request: main_models.DescribeOperatorListRequest,
    ) -> main_models.DescribeOperatorListResponse:
        runtime = RuntimeOptions()
        return self.describe_operator_list_with_options(request, runtime)

    async def describe_operator_list_async(
        self,
        request: main_models.DescribeOperatorListRequest,
    ) -> main_models.DescribeOperatorListResponse:
        runtime = RuntimeOptions()
        return await self.describe_operator_list_with_options_async(request, runtime)

    def describe_operator_list_by_scene_with_options(
        self,
        request: main_models.DescribeOperatorListBySceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorListBySceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperatorListByScene',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorListBySceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operator_list_by_scene_with_options_async(
        self,
        request: main_models.DescribeOperatorListBySceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorListBySceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperatorListByScene',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorListBySceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operator_list_by_scene(
        self,
        request: main_models.DescribeOperatorListBySceneRequest,
    ) -> main_models.DescribeOperatorListBySceneResponse:
        runtime = RuntimeOptions()
        return self.describe_operator_list_by_scene_with_options(request, runtime)

    async def describe_operator_list_by_scene_async(
        self,
        request: main_models.DescribeOperatorListBySceneRequest,
    ) -> main_models.DescribeOperatorListBySceneResponse:
        runtime = RuntimeOptions()
        return await self.describe_operator_list_by_scene_with_options_async(request, runtime)

    def describe_operator_list_by_type_with_options(
        self,
        request: main_models.DescribeOperatorListByTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorListByTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperatorListByType',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorListByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operator_list_by_type_with_options_async(
        self,
        request: main_models.DescribeOperatorListByTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorListByTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperatorListByType',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorListByTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operator_list_by_type(
        self,
        request: main_models.DescribeOperatorListByTypeRequest,
    ) -> main_models.DescribeOperatorListByTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_operator_list_by_type_with_options(request, runtime)

    async def describe_operator_list_by_type_async(
        self,
        request: main_models.DescribeOperatorListByTypeRequest,
    ) -> main_models.DescribeOperatorListByTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_operator_list_by_type_with_options_async(request, runtime)

    def describe_oss_auth_status_with_options(
        self,
        request: main_models.DescribeOssAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssAuthStatus',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_auth_status_with_options_async(
        self,
        request: main_models.DescribeOssAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssAuthStatus',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_auth_status(
        self,
        request: main_models.DescribeOssAuthStatusRequest,
    ) -> main_models.DescribeOssAuthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_oss_auth_status_with_options(request, runtime)

    async def describe_oss_auth_status_async(
        self,
        request: main_models.DescribeOssAuthStatusRequest,
    ) -> main_models.DescribeOssAuthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_oss_auth_status_with_options_async(request, runtime)

    def describe_oss_policy_with_options(
        self,
        request: main_models.DescribeOssPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_policy_with_options_async(
        self,
        request: main_models.DescribeOssPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_policy(
        self,
        request: main_models.DescribeOssPolicyRequest,
    ) -> main_models.DescribeOssPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_oss_policy_with_options(request, runtime)

    async def describe_oss_policy_async(
        self,
        request: main_models.DescribeOssPolicyRequest,
    ) -> main_models.DescribeOssPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_oss_policy_with_options_async(request, runtime)

    def describe_oss_token_with_options(
        self,
        request: main_models.DescribeOssTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.upload_type):
            query['uploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssToken',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_token_with_options_async(
        self,
        request: main_models.DescribeOssTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.upload_type):
            query['uploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssToken',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_token(
        self,
        request: main_models.DescribeOssTokenRequest,
    ) -> main_models.DescribeOssTokenResponse:
        runtime = RuntimeOptions()
        return self.describe_oss_token_with_options(request, runtime)

    async def describe_oss_token_async(
        self,
        request: main_models.DescribeOssTokenRequest,
    ) -> main_models.DescribeOssTokenResponse:
        runtime = RuntimeOptions()
        return await self.describe_oss_token_with_options_async(request, runtime)

    def describe_param_by_event_codes_with_options(
        self,
        request: main_models.DescribeParamByEventCodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParamByEventCodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.parma):
            query['parma'] = request.parma
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParamByEventCodes',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParamByEventCodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_param_by_event_codes_with_options_async(
        self,
        request: main_models.DescribeParamByEventCodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParamByEventCodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.parma):
            query['parma'] = request.parma
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParamByEventCodes',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParamByEventCodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_param_by_event_codes(
        self,
        request: main_models.DescribeParamByEventCodesRequest,
    ) -> main_models.DescribeParamByEventCodesResponse:
        runtime = RuntimeOptions()
        return self.describe_param_by_event_codes_with_options(request, runtime)

    async def describe_param_by_event_codes_async(
        self,
        request: main_models.DescribeParamByEventCodesRequest,
    ) -> main_models.DescribeParamByEventCodesResponse:
        runtime = RuntimeOptions()
        return await self.describe_param_by_event_codes_with_options_async(request, runtime)

    def describe_poc_oss_token_with_options(
        self,
        request: main_models.DescribePocOssTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePocOssTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePocOssToken',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePocOssTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_poc_oss_token_with_options_async(
        self,
        request: main_models.DescribePocOssTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePocOssTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePocOssToken',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePocOssTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_poc_oss_token(
        self,
        request: main_models.DescribePocOssTokenRequest,
    ) -> main_models.DescribePocOssTokenResponse:
        runtime = RuntimeOptions()
        return self.describe_poc_oss_token_with_options(request, runtime)

    async def describe_poc_oss_token_async(
        self,
        request: main_models.DescribePocOssTokenRequest,
    ) -> main_models.DescribePocOssTokenResponse:
        runtime = RuntimeOptions()
        return await self.describe_poc_oss_token_with_options_async(request, runtime)

    def describe_poc_task_list_with_options(
        self,
        request: main_models.DescribePocTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePocTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePocTaskList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePocTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_poc_task_list_with_options_async(
        self,
        request: main_models.DescribePocTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePocTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePocTaskList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePocTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_poc_task_list(
        self,
        request: main_models.DescribePocTaskListRequest,
    ) -> main_models.DescribePocTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_poc_task_list_with_options(request, runtime)

    async def describe_poc_task_list_async(
        self,
        request: main_models.DescribePocTaskListRequest,
    ) -> main_models.DescribePocTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_poc_task_list_with_options_async(request, runtime)

    def describe_private_stack_with_options(
        self,
        request: main_models.DescribePrivateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateStack',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_private_stack_with_options_async(
        self,
        request: main_models.DescribePrivateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateStack',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_private_stack(
        self,
        request: main_models.DescribePrivateStackRequest,
    ) -> main_models.DescribePrivateStackResponse:
        runtime = RuntimeOptions()
        return self.describe_private_stack_with_options(request, runtime)

    async def describe_private_stack_async(
        self,
        request: main_models.DescribePrivateStackRequest,
    ) -> main_models.DescribePrivateStackResponse:
        runtime = RuntimeOptions()
        return await self.describe_private_stack_with_options_async(request, runtime)

    def describe_query_variable_detail_with_options(
        self,
        request: main_models.DescribeQueryVariableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQueryVariableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQueryVariableDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQueryVariableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_query_variable_detail_with_options_async(
        self,
        request: main_models.DescribeQueryVariableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQueryVariableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQueryVariableDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQueryVariableDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_query_variable_detail(
        self,
        request: main_models.DescribeQueryVariableDetailRequest,
    ) -> main_models.DescribeQueryVariableDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_query_variable_detail_with_options(request, runtime)

    async def describe_query_variable_detail_async(
        self,
        request: main_models.DescribeQueryVariableDetailRequest,
    ) -> main_models.DescribeQueryVariableDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_query_variable_detail_with_options_async(request, runtime)

    def describe_query_variable_page_list_with_options(
        self,
        request: main_models.DescribeQueryVariablePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQueryVariablePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQueryVariablePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQueryVariablePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_query_variable_page_list_with_options_async(
        self,
        request: main_models.DescribeQueryVariablePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQueryVariablePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQueryVariablePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQueryVariablePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_query_variable_page_list(
        self,
        request: main_models.DescribeQueryVariablePageListRequest,
    ) -> main_models.DescribeQueryVariablePageListResponse:
        runtime = RuntimeOptions()
        return self.describe_query_variable_page_list_with_options(request, runtime)

    async def describe_query_variable_page_list_async(
        self,
        request: main_models.DescribeQueryVariablePageListRequest,
    ) -> main_models.DescribeQueryVariablePageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_query_variable_page_list_with_options_async(request, runtime)

    def describe_recommend_scene_variables_with_options(
        self,
        request: main_models.DescribeRecommendSceneVariablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendSceneVariablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_id):
            query['sampleId'] = request.sample_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendSceneVariables',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendSceneVariablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recommend_scene_variables_with_options_async(
        self,
        request: main_models.DescribeRecommendSceneVariablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendSceneVariablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_id):
            query['sampleId'] = request.sample_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendSceneVariables',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendSceneVariablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recommend_scene_variables(
        self,
        request: main_models.DescribeRecommendSceneVariablesRequest,
    ) -> main_models.DescribeRecommendSceneVariablesResponse:
        runtime = RuntimeOptions()
        return self.describe_recommend_scene_variables_with_options(request, runtime)

    async def describe_recommend_scene_variables_async(
        self,
        request: main_models.DescribeRecommendSceneVariablesRequest,
    ) -> main_models.DescribeRecommendSceneVariablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_recommend_scene_variables_with_options_async(request, runtime)

    def describe_recommend_task_detail_with_options(
        self,
        request: main_models.DescribeRecommendTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendTaskDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recommend_task_detail_with_options_async(
        self,
        request: main_models.DescribeRecommendTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendTaskDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recommend_task_detail(
        self,
        request: main_models.DescribeRecommendTaskDetailRequest,
    ) -> main_models.DescribeRecommendTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_recommend_task_detail_with_options(request, runtime)

    async def describe_recommend_task_detail_async(
        self,
        request: main_models.DescribeRecommendTaskDetailRequest,
    ) -> main_models.DescribeRecommendTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_recommend_task_detail_with_options_async(request, runtime)

    def describe_recommend_task_page_list_with_options(
        self,
        request: main_models.DescribeRecommendTaskPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendTaskPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendTaskPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendTaskPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recommend_task_page_list_with_options_async(
        self,
        request: main_models.DescribeRecommendTaskPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendTaskPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendTaskPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendTaskPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recommend_task_page_list(
        self,
        request: main_models.DescribeRecommendTaskPageListRequest,
    ) -> main_models.DescribeRecommendTaskPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_recommend_task_page_list_with_options(request, runtime)

    async def describe_recommend_task_page_list_async(
        self,
        request: main_models.DescribeRecommendTaskPageListRequest,
    ) -> main_models.DescribeRecommendTaskPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_recommend_task_page_list_with_options_async(request, runtime)

    def describe_recommend_variables_velocity_with_options(
        self,
        request: main_models.DescribeRecommendVariablesVelocityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendVariablesVelocityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        if not DaraCore.is_null(request.variable_ids_str):
            query['variableIdsStr'] = request.variable_ids_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendVariablesVelocity',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendVariablesVelocityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recommend_variables_velocity_with_options_async(
        self,
        request: main_models.DescribeRecommendVariablesVelocityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendVariablesVelocityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        if not DaraCore.is_null(request.variable_ids_str):
            query['variableIdsStr'] = request.variable_ids_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendVariablesVelocity',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendVariablesVelocityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recommend_variables_velocity(
        self,
        request: main_models.DescribeRecommendVariablesVelocityRequest,
    ) -> main_models.DescribeRecommendVariablesVelocityResponse:
        runtime = RuntimeOptions()
        return self.describe_recommend_variables_velocity_with_options(request, runtime)

    async def describe_recommend_variables_velocity_async(
        self,
        request: main_models.DescribeRecommendVariablesVelocityRequest,
    ) -> main_models.DescribeRecommendVariablesVelocityResponse:
        runtime = RuntimeOptions()
        return await self.describe_recommend_variables_velocity_with_options_async(request, runtime)

    def describe_recommend_velocities_with_options(
        self,
        request: main_models.DescribeRecommendVelocitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendVelocitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.code):
            query['code'] = request.code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendVelocities',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendVelocitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recommend_velocities_with_options_async(
        self,
        request: main_models.DescribeRecommendVelocitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecommendVelocitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.code):
            query['code'] = request.code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecommendVelocities',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecommendVelocitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recommend_velocities(
        self,
        request: main_models.DescribeRecommendVelocitiesRequest,
    ) -> main_models.DescribeRecommendVelocitiesResponse:
        runtime = RuntimeOptions()
        return self.describe_recommend_velocities_with_options(request, runtime)

    async def describe_recommend_velocities_async(
        self,
        request: main_models.DescribeRecommendVelocitiesRequest,
    ) -> main_models.DescribeRecommendVelocitiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_recommend_velocities_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_request_hit_with_options(
        self,
        request: main_models.DescribeRequestHitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRequestHitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRequestHit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRequestHitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_request_hit_with_options_async(
        self,
        request: main_models.DescribeRequestHitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRequestHitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRequestHit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRequestHitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_request_hit(
        self,
        request: main_models.DescribeRequestHitRequest,
    ) -> main_models.DescribeRequestHitResponse:
        runtime = RuntimeOptions()
        return self.describe_request_hit_with_options(request, runtime)

    async def describe_request_hit_async(
        self,
        request: main_models.DescribeRequestHitRequest,
    ) -> main_models.DescribeRequestHitResponse:
        runtime = RuntimeOptions()
        return await self.describe_request_hit_with_options_async(request, runtime)

    def describe_request_peak_report_with_options(
        self,
        request: main_models.DescribeRequestPeakReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRequestPeakReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRequestPeakReport',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRequestPeakReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_request_peak_report_with_options_async(
        self,
        request: main_models.DescribeRequestPeakReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRequestPeakReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRequestPeakReport',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRequestPeakReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_request_peak_report(
        self,
        request: main_models.DescribeRequestPeakReportRequest,
    ) -> main_models.DescribeRequestPeakReportResponse:
        runtime = RuntimeOptions()
        return self.describe_request_peak_report_with_options(request, runtime)

    async def describe_request_peak_report_async(
        self,
        request: main_models.DescribeRequestPeakReportRequest,
    ) -> main_models.DescribeRequestPeakReportResponse:
        runtime = RuntimeOptions()
        return await self.describe_request_peak_report_with_options_async(request, runtime)

    def describe_result_count_with_options(
        self,
        request: main_models.DescribeResultCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResultCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResultCount',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResultCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_result_count_with_options_async(
        self,
        request: main_models.DescribeResultCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResultCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResultCount',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResultCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_result_count(
        self,
        request: main_models.DescribeResultCountRequest,
    ) -> main_models.DescribeResultCountResponse:
        runtime = RuntimeOptions()
        return self.describe_result_count_with_options(request, runtime)

    async def describe_result_count_async(
        self,
        request: main_models.DescribeResultCountRequest,
    ) -> main_models.DescribeResultCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_result_count_with_options_async(request, runtime)

    def describe_risk_line_chart_with_options(
        self,
        request: main_models.DescribeRiskLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_line_chart_with_options_async(
        self,
        request: main_models.DescribeRiskLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskLineChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_line_chart(
        self,
        request: main_models.DescribeRiskLineChartRequest,
    ) -> main_models.DescribeRiskLineChartResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_line_chart_with_options(request, runtime)

    async def describe_risk_line_chart_async(
        self,
        request: main_models.DescribeRiskLineChartRequest,
    ) -> main_models.DescribeRiskLineChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_line_chart_with_options_async(request, runtime)

    def describe_risk_tags_line_chart_with_options(
        self,
        request: main_models.DescribeRiskTagsLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskTagsLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['EventCodes'] = request.event_codes
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskTagsLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskTagsLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_tags_line_chart_with_options_async(
        self,
        request: main_models.DescribeRiskTagsLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskTagsLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['EventCodes'] = request.event_codes
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskTagsLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskTagsLineChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_tags_line_chart(
        self,
        request: main_models.DescribeRiskTagsLineChartRequest,
    ) -> main_models.DescribeRiskTagsLineChartResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_tags_line_chart_with_options(request, runtime)

    async def describe_risk_tags_line_chart_async(
        self,
        request: main_models.DescribeRiskTagsLineChartRequest,
    ) -> main_models.DescribeRiskTagsLineChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_tags_line_chart_with_options_async(request, runtime)

    def describe_rule_bar_chart_with_options(
        self,
        request: main_models.DescribeRuleBarChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleBarChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleBarChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleBarChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_bar_chart_with_options_async(
        self,
        request: main_models.DescribeRuleBarChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleBarChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleBarChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleBarChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_bar_chart(
        self,
        request: main_models.DescribeRuleBarChartRequest,
    ) -> main_models.DescribeRuleBarChartResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_bar_chart_with_options(request, runtime)

    async def describe_rule_bar_chart_async(
        self,
        request: main_models.DescribeRuleBarChartRequest,
    ) -> main_models.DescribeRuleBarChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_bar_chart_with_options_async(request, runtime)

    def describe_rule_count_by_user_id_with_options(
        self,
        request: main_models.DescribeRuleCountByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleCountByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleCountByUserId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleCountByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_count_by_user_id_with_options_async(
        self,
        request: main_models.DescribeRuleCountByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleCountByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleCountByUserId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleCountByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_count_by_user_id(
        self,
        request: main_models.DescribeRuleCountByUserIdRequest,
    ) -> main_models.DescribeRuleCountByUserIdResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_count_by_user_id_with_options(request, runtime)

    async def describe_rule_count_by_user_id_async(
        self,
        request: main_models.DescribeRuleCountByUserIdRequest,
    ) -> main_models.DescribeRuleCountByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_count_by_user_id_with_options_async(request, runtime)

    def describe_rule_detail_by_rule_id_with_options(
        self,
        request: main_models.DescribeRuleDetailByRuleIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleDetailByRuleIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleDetailByRuleId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleDetailByRuleIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_detail_by_rule_id_with_options_async(
        self,
        request: main_models.DescribeRuleDetailByRuleIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleDetailByRuleIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleDetailByRuleId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleDetailByRuleIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_detail_by_rule_id(
        self,
        request: main_models.DescribeRuleDetailByRuleIdRequest,
    ) -> main_models.DescribeRuleDetailByRuleIdResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_detail_by_rule_id_with_options(request, runtime)

    async def describe_rule_detail_by_rule_id_async(
        self,
        request: main_models.DescribeRuleDetailByRuleIdRequest,
    ) -> main_models.DescribeRuleDetailByRuleIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_detail_by_rule_id_with_options_async(request, runtime)

    def describe_rule_hit_with_options(
        self,
        request: main_models.DescribeRuleHitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.request_time):
            query['requestTime'] = request.request_time
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_snapshot_id):
            query['ruleSnapshotId'] = request.rule_snapshot_id
        if not DaraCore.is_null(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hit_with_options_async(
        self,
        request: main_models.DescribeRuleHitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.request_time):
            query['requestTime'] = request.request_time
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_snapshot_id):
            query['ruleSnapshotId'] = request.rule_snapshot_id
        if not DaraCore.is_null(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hit(
        self,
        request: main_models.DescribeRuleHitRequest,
    ) -> main_models.DescribeRuleHitResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_hit_with_options(request, runtime)

    async def describe_rule_hit_async(
        self,
        request: main_models.DescribeRuleHitRequest,
    ) -> main_models.DescribeRuleHitResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_hit_with_options_async(request, runtime)

    def describe_rule_list_by_event_codes_list_with_options(
        self,
        request: main_models.DescribeRuleListByEventCodesListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleListByEventCodesListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleListByEventCodesList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleListByEventCodesListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_list_by_event_codes_list_with_options_async(
        self,
        request: main_models.DescribeRuleListByEventCodesListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleListByEventCodesListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleListByEventCodesList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleListByEventCodesListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_list_by_event_codes_list(
        self,
        request: main_models.DescribeRuleListByEventCodesListRequest,
    ) -> main_models.DescribeRuleListByEventCodesListResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_list_by_event_codes_list_with_options(request, runtime)

    async def describe_rule_list_by_event_codes_list_async(
        self,
        request: main_models.DescribeRuleListByEventCodesListRequest,
    ) -> main_models.DescribeRuleListByEventCodesListResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_list_by_event_codes_list_with_options_async(request, runtime)

    def describe_rule_page_list_with_options(
        self,
        request: main_models.DescribeRulePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRulePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_auth_type):
            query['ruleAuthType'] = request.rule_auth_type
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRulePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRulePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_page_list_with_options_async(
        self,
        request: main_models.DescribeRulePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRulePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_auth_type):
            query['ruleAuthType'] = request.rule_auth_type
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRulePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRulePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_page_list(
        self,
        request: main_models.DescribeRulePageListRequest,
    ) -> main_models.DescribeRulePageListResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_page_list_with_options(request, runtime)

    async def describe_rule_page_list_async(
        self,
        request: main_models.DescribeRulePageListRequest,
    ) -> main_models.DescribeRulePageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_page_list_with_options_async(request, runtime)

    def describe_rule_snapshot_with_options(
        self,
        request: main_models.DescribeRuleSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.snapshot_version):
            query['snapshotVersion'] = request.snapshot_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleSnapshot',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_snapshot_with_options_async(
        self,
        request: main_models.DescribeRuleSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.snapshot_version):
            query['snapshotVersion'] = request.snapshot_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleSnapshot',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_snapshot(
        self,
        request: main_models.DescribeRuleSnapshotRequest,
    ) -> main_models.DescribeRuleSnapshotResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_snapshot_with_options(request, runtime)

    async def describe_rule_snapshot_async(
        self,
        request: main_models.DescribeRuleSnapshotRequest,
    ) -> main_models.DescribeRuleSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_snapshot_with_options_async(request, runtime)

    def describe_rule_version_list_with_options(
        self,
        request: main_models.DescribeRuleVersionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleVersionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleVersionList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleVersionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_version_list_with_options_async(
        self,
        request: main_models.DescribeRuleVersionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleVersionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleVersionList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleVersionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_version_list(
        self,
        request: main_models.DescribeRuleVersionListRequest,
    ) -> main_models.DescribeRuleVersionListResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_version_list_with_options(request, runtime)

    async def describe_rule_version_list_async(
        self,
        request: main_models.DescribeRuleVersionListRequest,
    ) -> main_models.DescribeRuleVersionListResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_version_list_with_options_async(request, runtime)

    def describe_sdkdownload_list_with_options(
        self,
        request: main_models.DescribeSDKDownloadListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSDKDownloadListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.device_type):
            query['deviceType'] = request.device_type
        if not DaraCore.is_null(request.list_type):
            query['listType'] = request.list_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSDKDownloadList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSDKDownloadListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdkdownload_list_with_options_async(
        self,
        request: main_models.DescribeSDKDownloadListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSDKDownloadListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.device_type):
            query['deviceType'] = request.device_type
        if not DaraCore.is_null(request.list_type):
            query['listType'] = request.list_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSDKDownloadList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSDKDownloadListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sdkdownload_list(
        self,
        request: main_models.DescribeSDKDownloadListRequest,
    ) -> main_models.DescribeSDKDownloadListResponse:
        runtime = RuntimeOptions()
        return self.describe_sdkdownload_list_with_options(request, runtime)

    async def describe_sdkdownload_list_async(
        self,
        request: main_models.DescribeSDKDownloadListRequest,
    ) -> main_models.DescribeSDKDownloadListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sdkdownload_list_with_options_async(request, runtime)

    def describe_saf_console_with_options(
        self,
        request: main_models.DescribeSafConsoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafConsoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.service):
            query['service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafConsole',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafConsoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_saf_console_with_options_async(
        self,
        request: main_models.DescribeSafConsoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafConsoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.service):
            query['service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafConsole',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafConsoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_saf_console(
        self,
        request: main_models.DescribeSafConsoleRequest,
    ) -> main_models.DescribeSafConsoleResponse:
        runtime = RuntimeOptions()
        return self.describe_saf_console_with_options(request, runtime)

    async def describe_saf_console_async(
        self,
        request: main_models.DescribeSafConsoleRequest,
    ) -> main_models.DescribeSafConsoleResponse:
        runtime = RuntimeOptions()
        return await self.describe_saf_console_with_options_async(request, runtime)

    def describe_saf_de_order_with_options(
        self,
        request: main_models.DescribeSafDeOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafDeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafDeOrder',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafDeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_saf_de_order_with_options_async(
        self,
        request: main_models.DescribeSafDeOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafDeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafDeOrder',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafDeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_saf_de_order(
        self,
        request: main_models.DescribeSafDeOrderRequest,
    ) -> main_models.DescribeSafDeOrderResponse:
        runtime = RuntimeOptions()
        return self.describe_saf_de_order_with_options(request, runtime)

    async def describe_saf_de_order_async(
        self,
        request: main_models.DescribeSafDeOrderRequest,
    ) -> main_models.DescribeSafDeOrderResponse:
        runtime = RuntimeOptions()
        return await self.describe_saf_de_order_with_options_async(request, runtime)

    def describe_saf_order_with_options(
        self,
        request: main_models.DescribeSafOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.exact_product_code):
            query['exactProductCode'] = request.exact_product_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafOrder',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_saf_order_with_options_async(
        self,
        request: main_models.DescribeSafOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.exact_product_code):
            query['exactProductCode'] = request.exact_product_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafOrder',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_saf_order(
        self,
        request: main_models.DescribeSafOrderRequest,
    ) -> main_models.DescribeSafOrderResponse:
        runtime = RuntimeOptions()
        return self.describe_saf_order_with_options(request, runtime)

    async def describe_saf_order_async(
        self,
        request: main_models.DescribeSafOrderRequest,
    ) -> main_models.DescribeSafOrderResponse:
        runtime = RuntimeOptions()
        return await self.describe_saf_order_with_options_async(request, runtime)

    def describe_saf_start_config_with_options(
        self,
        request: main_models.DescribeSafStartConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafStartConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafStartConfig',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafStartConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_saf_start_config_with_options_async(
        self,
        request: main_models.DescribeSafStartConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafStartConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafStartConfig',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafStartConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_saf_start_config(
        self,
        request: main_models.DescribeSafStartConfigRequest,
    ) -> main_models.DescribeSafStartConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_saf_start_config_with_options(request, runtime)

    async def describe_saf_start_config_async(
        self,
        request: main_models.DescribeSafStartConfigRequest,
    ) -> main_models.DescribeSafStartConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_saf_start_config_with_options_async(request, runtime)

    def describe_saf_start_steps_with_options(
        self,
        request: main_models.DescribeSafStartStepsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafStartStepsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.aliyun_server):
            query['aliyunServer'] = request.aliyun_server
        if not DaraCore.is_null(request.device_types_str):
            query['deviceTypesStr'] = request.device_types_str
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.server_region):
            query['serverRegion'] = request.server_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafStartSteps',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafStartStepsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_saf_start_steps_with_options_async(
        self,
        request: main_models.DescribeSafStartStepsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafStartStepsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.aliyun_server):
            query['aliyunServer'] = request.aliyun_server
        if not DaraCore.is_null(request.device_types_str):
            query['deviceTypesStr'] = request.device_types_str
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.server_region):
            query['serverRegion'] = request.server_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafStartSteps',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafStartStepsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_saf_start_steps(
        self,
        request: main_models.DescribeSafStartStepsRequest,
    ) -> main_models.DescribeSafStartStepsResponse:
        runtime = RuntimeOptions()
        return self.describe_saf_start_steps_with_options(request, runtime)

    async def describe_saf_start_steps_async(
        self,
        request: main_models.DescribeSafStartStepsRequest,
    ) -> main_models.DescribeSafStartStepsResponse:
        runtime = RuntimeOptions()
        return await self.describe_saf_start_steps_with_options_async(request, runtime)

    def describe_saf_tag_list_with_options(
        self,
        request: main_models.DescribeSafTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.api_id):
            query['apiId'] = request.api_id
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafTagList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafTagListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_saf_tag_list_with_options_async(
        self,
        request: main_models.DescribeSafTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        if not DaraCore.is_null(request.api_id):
            query['apiId'] = request.api_id
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSafTagList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSafTagListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_saf_tag_list(
        self,
        request: main_models.DescribeSafTagListRequest,
    ) -> main_models.DescribeSafTagListResponse:
        runtime = RuntimeOptions()
        return self.describe_saf_tag_list_with_options(request, runtime)

    async def describe_saf_tag_list_async(
        self,
        request: main_models.DescribeSafTagListRequest,
    ) -> main_models.DescribeSafTagListResponse:
        runtime = RuntimeOptions()
        return await self.describe_saf_tag_list_with_options_async(request, runtime)

    def describe_sample_batch_oss_policy_with_options(
        self,
        request: main_models.DescribeSampleBatchOssPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleBatchOssPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_name):
            query['batchName'] = request.batch_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleBatchOssPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleBatchOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_batch_oss_policy_with_options_async(
        self,
        request: main_models.DescribeSampleBatchOssPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleBatchOssPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_name):
            query['batchName'] = request.batch_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleBatchOssPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleBatchOssPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_batch_oss_policy(
        self,
        request: main_models.DescribeSampleBatchOssPolicyRequest,
    ) -> main_models.DescribeSampleBatchOssPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_batch_oss_policy_with_options(request, runtime)

    async def describe_sample_batch_oss_policy_async(
        self,
        request: main_models.DescribeSampleBatchOssPolicyRequest,
    ) -> main_models.DescribeSampleBatchOssPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_batch_oss_policy_with_options_async(request, runtime)

    def describe_sample_data_by_batch_uuid_page_with_options(
        self,
        request: main_models.DescribeSampleDataByBatchUUidPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDataByBatchUUidPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_uuid):
            query['batchUuid'] = request.batch_uuid
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.update_begin_time):
            query['updateBeginTime'] = request.update_begin_time
        if not DaraCore.is_null(request.update_end_time):
            query['updateEndTime'] = request.update_end_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDataByBatchUUidPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDataByBatchUUidPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_data_by_batch_uuid_page_with_options_async(
        self,
        request: main_models.DescribeSampleDataByBatchUUidPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDataByBatchUUidPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_uuid):
            query['batchUuid'] = request.batch_uuid
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.update_begin_time):
            query['updateBeginTime'] = request.update_begin_time
        if not DaraCore.is_null(request.update_end_time):
            query['updateEndTime'] = request.update_end_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDataByBatchUUidPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDataByBatchUUidPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_data_by_batch_uuid_page(
        self,
        request: main_models.DescribeSampleDataByBatchUUidPageRequest,
    ) -> main_models.DescribeSampleDataByBatchUUidPageResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_data_by_batch_uuid_page_with_options(request, runtime)

    async def describe_sample_data_by_batch_uuid_page_async(
        self,
        request: main_models.DescribeSampleDataByBatchUUidPageRequest,
    ) -> main_models.DescribeSampleDataByBatchUUidPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_data_by_batch_uuid_page_with_options_async(request, runtime)

    def describe_sample_data_list_with_options(
        self,
        request: main_models.DescribeSampleDataListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDataListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.delete_tag):
            query['deleteTag'] = request.delete_tag
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query_content):
            query['queryContent'] = request.query_content
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_id):
            query['sampleId'] = request.sample_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDataList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_data_list_with_options_async(
        self,
        request: main_models.DescribeSampleDataListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDataListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.delete_tag):
            query['deleteTag'] = request.delete_tag
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query_content):
            query['queryContent'] = request.query_content
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_id):
            query['sampleId'] = request.sample_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDataList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_data_list(
        self,
        request: main_models.DescribeSampleDataListRequest,
    ) -> main_models.DescribeSampleDataListResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_data_list_with_options(request, runtime)

    async def describe_sample_data_list_async(
        self,
        request: main_models.DescribeSampleDataListRequest,
    ) -> main_models.DescribeSampleDataListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_data_list_with_options_async(request, runtime)

    def describe_sample_data_page_with_options(
        self,
        request: main_models.DescribeSampleDataPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDataPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.update_begin_time):
            query['updateBeginTime'] = request.update_begin_time
        if not DaraCore.is_null(request.update_end_time):
            query['updateEndTime'] = request.update_end_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDataPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDataPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_data_page_with_options_async(
        self,
        request: main_models.DescribeSampleDataPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDataPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.update_begin_time):
            query['updateBeginTime'] = request.update_begin_time
        if not DaraCore.is_null(request.update_end_time):
            query['updateEndTime'] = request.update_end_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDataPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDataPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_data_page(
        self,
        request: main_models.DescribeSampleDataPageRequest,
    ) -> main_models.DescribeSampleDataPageResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_data_page_with_options(request, runtime)

    async def describe_sample_data_page_async(
        self,
        request: main_models.DescribeSampleDataPageRequest,
    ) -> main_models.DescribeSampleDataPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_data_page_with_options_async(request, runtime)

    def describe_sample_demo_download_url_with_options(
        self,
        request: main_models.DescribeSampleDemoDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDemoDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDemoDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDemoDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_demo_download_url_with_options_async(
        self,
        request: main_models.DescribeSampleDemoDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDemoDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDemoDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDemoDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_demo_download_url(
        self,
        request: main_models.DescribeSampleDemoDownloadUrlRequest,
    ) -> main_models.DescribeSampleDemoDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_demo_download_url_with_options(request, runtime)

    async def describe_sample_demo_download_url_async(
        self,
        request: main_models.DescribeSampleDemoDownloadUrlRequest,
    ) -> main_models.DescribeSampleDemoDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_demo_download_url_with_options_async(request, runtime)

    def describe_sample_download_url_with_options(
        self,
        request: main_models.DescribeSampleDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_id):
            query['sampleId'] = request.sample_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_download_url_with_options_async(
        self,
        request: main_models.DescribeSampleDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_id):
            query['sampleId'] = request.sample_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_download_url(
        self,
        request: main_models.DescribeSampleDownloadUrlRequest,
    ) -> main_models.DescribeSampleDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_download_url_with_options(request, runtime)

    async def describe_sample_download_url_async(
        self,
        request: main_models.DescribeSampleDownloadUrlRequest,
    ) -> main_models.DescribeSampleDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_download_url_with_options_async(request, runtime)

    def describe_sample_info_with_options(
        self,
        request: main_models.DescribeSampleInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.versions):
            query['versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleInfo',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_info_with_options_async(
        self,
        request: main_models.DescribeSampleInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.versions):
            query['versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleInfo',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_info(
        self,
        request: main_models.DescribeSampleInfoRequest,
    ) -> main_models.DescribeSampleInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_info_with_options(request, runtime)

    async def describe_sample_info_async(
        self,
        request: main_models.DescribeSampleInfoRequest,
    ) -> main_models.DescribeSampleInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_info_with_options_async(request, runtime)

    def describe_sample_list_with_options(
        self,
        request: main_models.DescribeSampleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_type):
            query['sampleType'] = request.sample_type
        if not DaraCore.is_null(request.sample_value):
            query['sampleValue'] = request.sample_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_list_with_options_async(
        self,
        request: main_models.DescribeSampleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_type):
            query['sampleType'] = request.sample_type
        if not DaraCore.is_null(request.sample_value):
            query['sampleValue'] = request.sample_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_list(
        self,
        request: main_models.DescribeSampleListRequest,
    ) -> main_models.DescribeSampleListResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_list_with_options(request, runtime)

    async def describe_sample_list_async(
        self,
        request: main_models.DescribeSampleListRequest,
    ) -> main_models.DescribeSampleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_list_with_options_async(request, runtime)

    def describe_sample_scene_list_with_options(
        self,
        request: main_models.DescribeSampleSceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleSceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleSceneList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_scene_list_with_options_async(
        self,
        request: main_models.DescribeSampleSceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleSceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleSceneList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_scene_list(
        self,
        request: main_models.DescribeSampleSceneListRequest,
    ) -> main_models.DescribeSampleSceneListResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_scene_list_with_options(request, runtime)

    async def describe_sample_scene_list_async(
        self,
        request: main_models.DescribeSampleSceneListRequest,
    ) -> main_models.DescribeSampleSceneListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_scene_list_with_options_async(request, runtime)

    def describe_sample_tag_list_with_options(
        self,
        request: main_models.DescribeSampleTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleTagList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleTagListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_tag_list_with_options_async(
        self,
        request: main_models.DescribeSampleTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleTagList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleTagListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_tag_list(
        self,
        request: main_models.DescribeSampleTagListRequest,
    ) -> main_models.DescribeSampleTagListResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_tag_list_with_options(request, runtime)

    async def describe_sample_tag_list_async(
        self,
        request: main_models.DescribeSampleTagListRequest,
    ) -> main_models.DescribeSampleTagListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_tag_list_with_options_async(request, runtime)

    def describe_sample_upload_policy_with_options(
        self,
        request: main_models.DescribeSampleUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleUploadPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_upload_policy_with_options_async(
        self,
        request: main_models.DescribeSampleUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSampleUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSampleUploadPolicy',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSampleUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_upload_policy(
        self,
        request: main_models.DescribeSampleUploadPolicyRequest,
    ) -> main_models.DescribeSampleUploadPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_sample_upload_policy_with_options(request, runtime)

    async def describe_sample_upload_policy_async(
        self,
        request: main_models.DescribeSampleUploadPolicyRequest,
    ) -> main_models.DescribeSampleUploadPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_sample_upload_policy_with_options_async(request, runtime)

    def describe_samplebatch_page_with_options(
        self,
        request: main_models.DescribeSamplebatchPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSamplebatchPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSamplebatchPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSamplebatchPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_samplebatch_page_with_options_async(
        self,
        request: main_models.DescribeSamplebatchPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSamplebatchPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.data_value):
            query['dataValue'] = request.data_value
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSamplebatchPage',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSamplebatchPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_samplebatch_page(
        self,
        request: main_models.DescribeSamplebatchPageRequest,
    ) -> main_models.DescribeSamplebatchPageResponse:
        runtime = RuntimeOptions()
        return self.describe_samplebatch_page_with_options(request, runtime)

    async def describe_samplebatch_page_async(
        self,
        request: main_models.DescribeSamplebatchPageRequest,
    ) -> main_models.DescribeSamplebatchPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_samplebatch_page_with_options_async(request, runtime)

    def describe_scene_all_event_name_code_list_with_options(
        self,
        request: main_models.DescribeSceneAllEventNameCodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneAllEventNameCodeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneAllEventNameCodeList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneAllEventNameCodeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_all_event_name_code_list_with_options_async(
        self,
        request: main_models.DescribeSceneAllEventNameCodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneAllEventNameCodeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneAllEventNameCodeList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneAllEventNameCodeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_all_event_name_code_list(
        self,
        request: main_models.DescribeSceneAllEventNameCodeListRequest,
    ) -> main_models.DescribeSceneAllEventNameCodeListResponse:
        runtime = RuntimeOptions()
        return self.describe_scene_all_event_name_code_list_with_options(request, runtime)

    async def describe_scene_all_event_name_code_list_async(
        self,
        request: main_models.DescribeSceneAllEventNameCodeListRequest,
    ) -> main_models.DescribeSceneAllEventNameCodeListResponse:
        runtime = RuntimeOptions()
        return await self.describe_scene_all_event_name_code_list_with_options_async(request, runtime)

    def describe_scene_event_page_list_with_options(
        self,
        request: main_models.DescribeSceneEventPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneEventPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name_or_code):
            query['nameOrCode'] = request.name_or_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneEventPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneEventPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_event_page_list_with_options_async(
        self,
        request: main_models.DescribeSceneEventPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneEventPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.name_or_code):
            query['nameOrCode'] = request.name_or_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneEventPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneEventPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_event_page_list(
        self,
        request: main_models.DescribeSceneEventPageListRequest,
    ) -> main_models.DescribeSceneEventPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_scene_event_page_list_with_options(request, runtime)

    async def describe_scene_event_page_list_async(
        self,
        request: main_models.DescribeSceneEventPageListRequest,
    ) -> main_models.DescribeSceneEventPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_scene_event_page_list_with_options_async(request, runtime)

    def describe_scene_rule_page_list_with_options(
        self,
        request: main_models.DescribeSceneRulePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneRulePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_auth_type):
            query['ruleAuthType'] = request.rule_auth_type
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneRulePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneRulePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_rule_page_list_with_options_async(
        self,
        request: main_models.DescribeSceneRulePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneRulePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_auth_type):
            query['ruleAuthType'] = request.rule_auth_type
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneRulePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneRulePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_rule_page_list(
        self,
        request: main_models.DescribeSceneRulePageListRequest,
    ) -> main_models.DescribeSceneRulePageListResponse:
        runtime = RuntimeOptions()
        return self.describe_scene_rule_page_list_with_options(request, runtime)

    async def describe_scene_rule_page_list_async(
        self,
        request: main_models.DescribeSceneRulePageListRequest,
    ) -> main_models.DescribeSceneRulePageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_scene_rule_page_list_with_options_async(request, runtime)

    def describe_score_list_with_options(
        self,
        request: main_models.DescribeScoreListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScoreListResponse:
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
            action = 'DescribeScoreList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScoreListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_score_list_with_options_async(
        self,
        request: main_models.DescribeScoreListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScoreListResponse:
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
            action = 'DescribeScoreList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScoreListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_score_list(
        self,
        request: main_models.DescribeScoreListRequest,
    ) -> main_models.DescribeScoreListResponse:
        runtime = RuntimeOptions()
        return self.describe_score_list_with_options(request, runtime)

    async def describe_score_list_async(
        self,
        request: main_models.DescribeScoreListRequest,
    ) -> main_models.DescribeScoreListResponse:
        runtime = RuntimeOptions()
        return await self.describe_score_list_with_options_async(request, runtime)

    def describe_score_section_num_line_chart_with_options(
        self,
        request: main_models.DescribeScoreSectionNumLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScoreSectionNumLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScoreSectionNumLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScoreSectionNumLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_score_section_num_line_chart_with_options_async(
        self,
        request: main_models.DescribeScoreSectionNumLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScoreSectionNumLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScoreSectionNumLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScoreSectionNumLineChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_score_section_num_line_chart(
        self,
        request: main_models.DescribeScoreSectionNumLineChartRequest,
    ) -> main_models.DescribeScoreSectionNumLineChartResponse:
        runtime = RuntimeOptions()
        return self.describe_score_section_num_line_chart_with_options(request, runtime)

    async def describe_score_section_num_line_chart_async(
        self,
        request: main_models.DescribeScoreSectionNumLineChartRequest,
    ) -> main_models.DescribeScoreSectionNumLineChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_score_section_num_line_chart_with_options_async(request, runtime)

    def describe_score_section_pie_chart_with_options(
        self,
        request: main_models.DescribeScoreSectionPieChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScoreSectionPieChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_type):
            query['eventType'] = request.event_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScoreSectionPieChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScoreSectionPieChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_score_section_pie_chart_with_options_async(
        self,
        request: main_models.DescribeScoreSectionPieChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScoreSectionPieChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.event_type):
            query['eventType'] = request.event_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScoreSectionPieChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScoreSectionPieChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_score_section_pie_chart(
        self,
        request: main_models.DescribeScoreSectionPieChartRequest,
    ) -> main_models.DescribeScoreSectionPieChartResponse:
        runtime = RuntimeOptions()
        return self.describe_score_section_pie_chart_with_options(request, runtime)

    async def describe_score_section_pie_chart_async(
        self,
        request: main_models.DescribeScoreSectionPieChartRequest,
    ) -> main_models.DescribeScoreSectionPieChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_score_section_pie_chart_with_options_async(request, runtime)

    def describe_score_section_ratio_line_chart_with_options(
        self,
        request: main_models.DescribeScoreSectionRatioLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScoreSectionRatioLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScoreSectionRatioLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScoreSectionRatioLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_score_section_ratio_line_chart_with_options_async(
        self,
        request: main_models.DescribeScoreSectionRatioLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScoreSectionRatioLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScoreSectionRatioLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScoreSectionRatioLineChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_score_section_ratio_line_chart(
        self,
        request: main_models.DescribeScoreSectionRatioLineChartRequest,
    ) -> main_models.DescribeScoreSectionRatioLineChartResponse:
        runtime = RuntimeOptions()
        return self.describe_score_section_ratio_line_chart_with_options(request, runtime)

    async def describe_score_section_ratio_line_chart_async(
        self,
        request: main_models.DescribeScoreSectionRatioLineChartRequest,
    ) -> main_models.DescribeScoreSectionRatioLineChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_score_section_ratio_line_chart_with_options_async(request, runtime)

    def describe_select_item_with_options(
        self,
        request: main_models.DescribeSelectItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSelectItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSelectItem',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSelectItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_select_item_with_options_async(
        self,
        request: main_models.DescribeSelectItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSelectItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSelectItem',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSelectItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_select_item(
        self,
        request: main_models.DescribeSelectItemRequest,
    ) -> main_models.DescribeSelectItemResponse:
        runtime = RuntimeOptions()
        return self.describe_select_item_with_options(request, runtime)

    async def describe_select_item_async(
        self,
        request: main_models.DescribeSelectItemRequest,
    ) -> main_models.DescribeSelectItemResponse:
        runtime = RuntimeOptions()
        return await self.describe_select_item_with_options_async(request, runtime)

    def describe_service_app_key_with_options(
        self,
        request: main_models.DescribeServiceAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceAppKey',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_app_key_with_options_async(
        self,
        request: main_models.DescribeServiceAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceAppKey',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_app_key(
        self,
        request: main_models.DescribeServiceAppKeyRequest,
    ) -> main_models.DescribeServiceAppKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_service_app_key_with_options(request, runtime)

    async def describe_service_app_key_async(
        self,
        request: main_models.DescribeServiceAppKeyRequest,
    ) -> main_models.DescribeServiceAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_service_app_key_with_options_async(request, runtime)

    def describe_service_code_name_with_options(
        self,
        request: main_models.DescribeServiceCodeNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceCodeNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tab):
            query['Tab'] = request.tab
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceCodeName',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceCodeNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_code_name_with_options_async(
        self,
        request: main_models.DescribeServiceCodeNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceCodeNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tab):
            query['Tab'] = request.tab
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceCodeName',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceCodeNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_code_name(
        self,
        request: main_models.DescribeServiceCodeNameRequest,
    ) -> main_models.DescribeServiceCodeNameResponse:
        runtime = RuntimeOptions()
        return self.describe_service_code_name_with_options(request, runtime)

    async def describe_service_code_name_async(
        self,
        request: main_models.DescribeServiceCodeNameRequest,
    ) -> main_models.DescribeServiceCodeNameResponse:
        runtime = RuntimeOptions()
        return await self.describe_service_code_name_with_options_async(request, runtime)

    def describe_service_list_with_options(
        self,
        request: main_models.DescribeServiceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_list_with_options_async(
        self,
        request: main_models.DescribeServiceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_list(
        self,
        request: main_models.DescribeServiceListRequest,
    ) -> main_models.DescribeServiceListResponse:
        runtime = RuntimeOptions()
        return self.describe_service_list_with_options(request, runtime)

    async def describe_service_list_async(
        self,
        request: main_models.DescribeServiceListRequest,
    ) -> main_models.DescribeServiceListResponse:
        runtime = RuntimeOptions()
        return await self.describe_service_list_with_options_async(request, runtime)

    def describe_simulation_predit_info_with_options(
        self,
        request: main_models.DescribeSimulationPreditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimulationPreditInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rules_str):
            query['rulesStr'] = request.rules_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimulationPreditInfo',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimulationPreditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_simulation_predit_info_with_options_async(
        self,
        request: main_models.DescribeSimulationPreditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimulationPreditInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rules_str):
            query['rulesStr'] = request.rules_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimulationPreditInfo',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimulationPreditInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_simulation_predit_info(
        self,
        request: main_models.DescribeSimulationPreditInfoRequest,
    ) -> main_models.DescribeSimulationPreditInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_simulation_predit_info_with_options(request, runtime)

    async def describe_simulation_predit_info_async(
        self,
        request: main_models.DescribeSimulationPreditInfoRequest,
    ) -> main_models.DescribeSimulationPreditInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_simulation_predit_info_with_options_async(request, runtime)

    def describe_simulation_task_count_with_options(
        self,
        request: main_models.DescribeSimulationTaskCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimulationTaskCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_config):
            query['dataSourceConfig'] = request.data_source_config
        if not DaraCore.is_null(request.data_source_type):
            query['dataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.filters_str):
            query['filtersStr'] = request.filters_str
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimulationTaskCount',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimulationTaskCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_simulation_task_count_with_options_async(
        self,
        request: main_models.DescribeSimulationTaskCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimulationTaskCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_config):
            query['dataSourceConfig'] = request.data_source_config
        if not DaraCore.is_null(request.data_source_type):
            query['dataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.filters_str):
            query['filtersStr'] = request.filters_str
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimulationTaskCount',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimulationTaskCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_simulation_task_count(
        self,
        request: main_models.DescribeSimulationTaskCountRequest,
    ) -> main_models.DescribeSimulationTaskCountResponse:
        runtime = RuntimeOptions()
        return self.describe_simulation_task_count_with_options(request, runtime)

    async def describe_simulation_task_count_async(
        self,
        request: main_models.DescribeSimulationTaskCountRequest,
    ) -> main_models.DescribeSimulationTaskCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_simulation_task_count_with_options_async(request, runtime)

    def describe_simulation_task_list_with_options(
        self,
        request: main_models.DescribeSimulationTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimulationTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimulationTaskList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimulationTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_simulation_task_list_with_options_async(
        self,
        request: main_models.DescribeSimulationTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimulationTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimulationTaskList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimulationTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_simulation_task_list(
        self,
        request: main_models.DescribeSimulationTaskListRequest,
    ) -> main_models.DescribeSimulationTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_simulation_task_list_with_options(request, runtime)

    async def describe_simulation_task_list_async(
        self,
        request: main_models.DescribeSimulationTaskListRequest,
    ) -> main_models.DescribeSimulationTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_simulation_task_list_with_options_async(request, runtime)

    def describe_sls_url_config_with_options(
        self,
        request: main_models.DescribeSlsUrlConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsUrlConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsUrlConfig',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_url_config_with_options_async(
        self,
        request: main_models.DescribeSlsUrlConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsUrlConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsUrlConfig',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_url_config(
        self,
        request: main_models.DescribeSlsUrlConfigRequest,
    ) -> main_models.DescribeSlsUrlConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_url_config_with_options(request, runtime)

    async def describe_sls_url_config_async(
        self,
        request: main_models.DescribeSlsUrlConfigRequest,
    ) -> main_models.DescribeSlsUrlConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_url_config_with_options_async(request, runtime)

    def describe_support_rule_list_with_options(
        self,
        request: main_models.DescribeSupportRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSupportRuleList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_support_rule_list_with_options_async(
        self,
        request: main_models.DescribeSupportRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSupportRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSupportRuleList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSupportRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_support_rule_list(
        self,
        request: main_models.DescribeSupportRuleListRequest,
    ) -> main_models.DescribeSupportRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_support_rule_list_with_options(request, runtime)

    async def describe_support_rule_list_async(
        self,
        request: main_models.DescribeSupportRuleListRequest,
    ) -> main_models.DescribeSupportRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_support_rule_list_with_options_async(request, runtime)

    def describe_tag_list_with_options(
        self,
        request: main_models.DescribeTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_list_with_options_async(
        self,
        request: main_models.DescribeTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_list(
        self,
        request: main_models.DescribeTagListRequest,
    ) -> main_models.DescribeTagListResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_list_with_options(request, runtime)

    async def describe_tag_list_async(
        self,
        request: main_models.DescribeTagListRequest,
    ) -> main_models.DescribeTagListResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_list_with_options_async(request, runtime)

    def describe_tags_bar_chart_with_options(
        self,
        request: main_models.DescribeTagsBarChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsBarChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.result):
            query['result'] = request.result
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsBarChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsBarChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_bar_chart_with_options_async(
        self,
        request: main_models.DescribeTagsBarChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsBarChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.result):
            query['result'] = request.result
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsBarChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsBarChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags_bar_chart(
        self,
        request: main_models.DescribeTagsBarChartRequest,
    ) -> main_models.DescribeTagsBarChartResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_bar_chart_with_options(request, runtime)

    async def describe_tags_bar_chart_async(
        self,
        request: main_models.DescribeTagsBarChartRequest,
    ) -> main_models.DescribeTagsBarChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_bar_chart_with_options_async(request, runtime)

    def describe_tags_fluctuation_with_options(
        self,
        request: main_models.DescribeTagsFluctuationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsFluctuationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsFluctuation',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsFluctuationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_fluctuation_with_options_async(
        self,
        request: main_models.DescribeTagsFluctuationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsFluctuationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsFluctuation',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsFluctuationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags_fluctuation(
        self,
        request: main_models.DescribeTagsFluctuationRequest,
    ) -> main_models.DescribeTagsFluctuationResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_fluctuation_with_options(request, runtime)

    async def describe_tags_fluctuation_async(
        self,
        request: main_models.DescribeTagsFluctuationRequest,
    ) -> main_models.DescribeTagsFluctuationResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_fluctuation_with_options_async(request, runtime)

    def describe_tags_list_with_options(
        self,
        request: main_models.DescribeTagsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_list_with_options_async(
        self,
        request: main_models.DescribeTagsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags_list(
        self,
        request: main_models.DescribeTagsListRequest,
    ) -> main_models.DescribeTagsListResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_list_with_options(request, runtime)

    async def describe_tags_list_async(
        self,
        request: main_models.DescribeTagsListRequest,
    ) -> main_models.DescribeTagsListResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_list_with_options_async(request, runtime)

    def describe_tags_num_line_chart_with_options(
        self,
        request: main_models.DescribeTagsNumLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsNumLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsNumLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsNumLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_num_line_chart_with_options_async(
        self,
        request: main_models.DescribeTagsNumLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsNumLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsNumLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsNumLineChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags_num_line_chart(
        self,
        request: main_models.DescribeTagsNumLineChartRequest,
    ) -> main_models.DescribeTagsNumLineChartResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_num_line_chart_with_options(request, runtime)

    async def describe_tags_num_line_chart_async(
        self,
        request: main_models.DescribeTagsNumLineChartRequest,
    ) -> main_models.DescribeTagsNumLineChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_num_line_chart_with_options_async(request, runtime)

    def describe_tags_ratio_line_chart_with_options(
        self,
        request: main_models.DescribeTagsRatioLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsRatioLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsRatioLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsRatioLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_ratio_line_chart_with_options_async(
        self,
        request: main_models.DescribeTagsRatioLineChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsRatioLineChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsRatioLineChart',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsRatioLineChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags_ratio_line_chart(
        self,
        request: main_models.DescribeTagsRatioLineChartRequest,
    ) -> main_models.DescribeTagsRatioLineChartResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_ratio_line_chart_with_options(request, runtime)

    async def describe_tags_ratio_line_chart_async(
        self,
        request: main_models.DescribeTagsRatioLineChartRequest,
    ) -> main_models.DescribeTagsRatioLineChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_ratio_line_chart_with_options_async(request, runtime)

    def describe_tags_trend_with_options(
        self,
        request: main_models.DescribeTagsTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.result):
            query['result'] = request.result
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsTrend',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_trend_with_options_async(
        self,
        request: main_models.DescribeTagsTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.result):
            query['result'] = request.result
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagsTrend',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags_trend(
        self,
        request: main_models.DescribeTagsTrendRequest,
    ) -> main_models.DescribeTagsTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_trend_with_options(request, runtime)

    async def describe_tags_trend_async(
        self,
        request: main_models.DescribeTagsTrendRequest,
    ) -> main_models.DescribeTagsTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_trend_with_options_async(request, runtime)

    def describe_task_list_with_options(
        self,
        request: main_models.DescribeTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.is_page):
            query['IsPage'] = request.is_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTaskList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_list_with_options_async(
        self,
        request: main_models.DescribeTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.is_page):
            query['IsPage'] = request.is_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTaskList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task_list(
        self,
        request: main_models.DescribeTaskListRequest,
    ) -> main_models.DescribeTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_task_list_with_options(request, runtime)

    async def describe_task_list_async(
        self,
        request: main_models.DescribeTaskListRequest,
    ) -> main_models.DescribeTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_task_list_with_options_async(request, runtime)

    def describe_task_log_list_with_options(
        self,
        request: main_models.DescribeTaskLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.is_page):
            query['IsPage'] = request.is_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_log_id):
            query['TaskLogId'] = request.task_log_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTaskLogList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_log_list_with_options_async(
        self,
        request: main_models.DescribeTaskLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.is_page):
            query['IsPage'] = request.is_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_log_id):
            query['TaskLogId'] = request.task_log_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTaskLogList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task_log_list(
        self,
        request: main_models.DescribeTaskLogListRequest,
    ) -> main_models.DescribeTaskLogListResponse:
        runtime = RuntimeOptions()
        return self.describe_task_log_list_with_options(request, runtime)

    async def describe_task_log_list_async(
        self,
        request: main_models.DescribeTaskLogListRequest,
    ) -> main_models.DescribeTaskLogListResponse:
        runtime = RuntimeOptions()
        return await self.describe_task_log_list_with_options_async(request, runtime)

    def describe_template_count_with_options(
        self,
        request: main_models.DescribeTemplateCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateCount',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_count_with_options_async(
        self,
        request: main_models.DescribeTemplateCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateCount',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_count(
        self,
        request: main_models.DescribeTemplateCountRequest,
    ) -> main_models.DescribeTemplateCountResponse:
        runtime = RuntimeOptions()
        return self.describe_template_count_with_options(request, runtime)

    async def describe_template_count_async(
        self,
        request: main_models.DescribeTemplateCountRequest,
    ) -> main_models.DescribeTemplateCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_template_count_with_options_async(request, runtime)

    def describe_template_download_with_options(
        self,
        request: main_models.DescribeTemplateDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateDownload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_download_with_options_async(
        self,
        request: main_models.DescribeTemplateDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateDownload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_download(
        self,
        request: main_models.DescribeTemplateDownloadRequest,
    ) -> main_models.DescribeTemplateDownloadResponse:
        runtime = RuntimeOptions()
        return self.describe_template_download_with_options(request, runtime)

    async def describe_template_download_async(
        self,
        request: main_models.DescribeTemplateDownloadRequest,
    ) -> main_models.DescribeTemplateDownloadResponse:
        runtime = RuntimeOptions()
        return await self.describe_template_download_with_options_async(request, runtime)

    def describe_template_page_list_with_options(
        self,
        request: main_models.DescribeTemplatePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplatePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.template_search_item):
            query['templateSearchItem'] = request.template_search_item
        if not DaraCore.is_null(request.template_status):
            query['templateStatus'] = request.template_status
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplatePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplatePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_page_list_with_options_async(
        self,
        request: main_models.DescribeTemplatePageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplatePageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.template_search_item):
            query['templateSearchItem'] = request.template_search_item
        if not DaraCore.is_null(request.template_status):
            query['templateStatus'] = request.template_status
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplatePageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplatePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_page_list(
        self,
        request: main_models.DescribeTemplatePageListRequest,
    ) -> main_models.DescribeTemplatePageListResponse:
        runtime = RuntimeOptions()
        return self.describe_template_page_list_with_options(request, runtime)

    async def describe_template_page_list_async(
        self,
        request: main_models.DescribeTemplatePageListRequest,
    ) -> main_models.DescribeTemplatePageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_template_page_list_with_options_async(request, runtime)

    def describe_used_service_with_options(
        self,
        request: main_models.DescribeUsedServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsedServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsedService',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsedServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_used_service_with_options_async(
        self,
        request: main_models.DescribeUsedServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsedServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsedService',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsedServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_used_service(
        self,
        request: main_models.DescribeUsedServiceRequest,
    ) -> main_models.DescribeUsedServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_used_service_with_options(request, runtime)

    async def describe_used_service_async(
        self,
        request: main_models.DescribeUsedServiceRequest,
    ) -> main_models.DescribeUsedServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_used_service_with_options_async(request, runtime)

    def describe_user_info_with_options(
        self,
        request: main_models.DescribeUserInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserInfo',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_info_with_options_async(
        self,
        request: main_models.DescribeUserInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserInfo',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_info(
        self,
        request: main_models.DescribeUserInfoRequest,
    ) -> main_models.DescribeUserInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_user_info_with_options(request, runtime)

    async def describe_user_info_async(
        self,
        request: main_models.DescribeUserInfoRequest,
    ) -> main_models.DescribeUserInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_info_with_options_async(request, runtime)

    def describe_variable_bind_detail_with_options(
        self,
        request: main_models.DescribeVariableBindDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableBindDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.define_id):
            query['defineId'] = request.define_id
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableBindDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableBindDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_variable_bind_detail_with_options_async(
        self,
        request: main_models.DescribeVariableBindDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableBindDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.define_id):
            query['defineId'] = request.define_id
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableBindDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableBindDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_variable_bind_detail(
        self,
        request: main_models.DescribeVariableBindDetailRequest,
    ) -> main_models.DescribeVariableBindDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_variable_bind_detail_with_options(request, runtime)

    async def describe_variable_bind_detail_async(
        self,
        request: main_models.DescribeVariableBindDetailRequest,
    ) -> main_models.DescribeVariableBindDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_variable_bind_detail_with_options_async(request, runtime)

    def describe_variable_detail_with_options(
        self,
        request: main_models.DescribeVariableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_variable_detail_with_options_async(
        self,
        request: main_models.DescribeVariableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_variable_detail(
        self,
        request: main_models.DescribeVariableDetailRequest,
    ) -> main_models.DescribeVariableDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_variable_detail_with_options(request, runtime)

    async def describe_variable_detail_async(
        self,
        request: main_models.DescribeVariableDetailRequest,
    ) -> main_models.DescribeVariableDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_variable_detail_with_options_async(request, runtime)

    def describe_variable_fee_with_options(
        self,
        request: main_models.DescribeVariableFeeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableFeeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.ids):
            query['ids'] = request.ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableFee',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableFeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_variable_fee_with_options_async(
        self,
        request: main_models.DescribeVariableFeeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableFeeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.ids):
            query['ids'] = request.ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableFee',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableFeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_variable_fee(
        self,
        request: main_models.DescribeVariableFeeRequest,
    ) -> main_models.DescribeVariableFeeResponse:
        runtime = RuntimeOptions()
        return self.describe_variable_fee_with_options(request, runtime)

    async def describe_variable_fee_async(
        self,
        request: main_models.DescribeVariableFeeRequest,
    ) -> main_models.DescribeVariableFeeResponse:
        runtime = RuntimeOptions()
        return await self.describe_variable_fee_with_options_async(request, runtime)

    def describe_variable_list_with_options(
        self,
        request: main_models.DescribeVariableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.ref_obj_id):
            query['refObjId'] = request.ref_obj_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.types_str):
            query['typesStr'] = request.types_str
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_variable_list_with_options_async(
        self,
        request: main_models.DescribeVariableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.ref_obj_id):
            query['refObjId'] = request.ref_obj_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.types_str):
            query['typesStr'] = request.types_str
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_variable_list(
        self,
        request: main_models.DescribeVariableListRequest,
    ) -> main_models.DescribeVariableListResponse:
        runtime = RuntimeOptions()
        return self.describe_variable_list_with_options(request, runtime)

    async def describe_variable_list_async(
        self,
        request: main_models.DescribeVariableListRequest,
    ) -> main_models.DescribeVariableListResponse:
        runtime = RuntimeOptions()
        return await self.describe_variable_list_with_options_async(request, runtime)

    def describe_variable_market_list_with_options(
        self,
        request: main_models.DescribeVariableMarketListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableMarketListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.charging_mode):
            query['chargingMode'] = request.charging_mode
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.paging):
            query['paging'] = request.paging
        if not DaraCore.is_null(request.query_content):
            query['queryContent'] = request.query_content
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scenes_str):
            query['scenesStr'] = request.scenes_str
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableMarketList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableMarketListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_variable_market_list_with_options_async(
        self,
        request: main_models.DescribeVariableMarketListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableMarketListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.charging_mode):
            query['chargingMode'] = request.charging_mode
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.paging):
            query['paging'] = request.paging
        if not DaraCore.is_null(request.query_content):
            query['queryContent'] = request.query_content
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scenes_str):
            query['scenesStr'] = request.scenes_str
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableMarketList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableMarketListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_variable_market_list(
        self,
        request: main_models.DescribeVariableMarketListRequest,
    ) -> main_models.DescribeVariableMarketListResponse:
        runtime = RuntimeOptions()
        return self.describe_variable_market_list_with_options(request, runtime)

    async def describe_variable_market_list_async(
        self,
        request: main_models.DescribeVariableMarketListRequest,
    ) -> main_models.DescribeVariableMarketListResponse:
        runtime = RuntimeOptions()
        return await self.describe_variable_market_list_with_options_async(request, runtime)

    def describe_variable_scene_list_with_options(
        self,
        request: main_models.DescribeVariableSceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableSceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.biz_type):
            query['bizType'] = request.biz_type
        if not DaraCore.is_null(request.config_key):
            query['configKey'] = request.config_key
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.paging):
            query['paging'] = request.paging
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableSceneList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_variable_scene_list_with_options_async(
        self,
        request: main_models.DescribeVariableSceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableSceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.biz_type):
            query['bizType'] = request.biz_type
        if not DaraCore.is_null(request.config_key):
            query['configKey'] = request.config_key
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.paging):
            query['paging'] = request.paging
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableSceneList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_variable_scene_list(
        self,
        request: main_models.DescribeVariableSceneListRequest,
    ) -> main_models.DescribeVariableSceneListResponse:
        runtime = RuntimeOptions()
        return self.describe_variable_scene_list_with_options(request, runtime)

    async def describe_variable_scene_list_async(
        self,
        request: main_models.DescribeVariableSceneListRequest,
    ) -> main_models.DescribeVariableSceneListResponse:
        runtime = RuntimeOptions()
        return await self.describe_variable_scene_list_with_options_async(request, runtime)

    def describe_variable_version_detail_with_options(
        self,
        request: main_models.DescribeVariableVersionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableVersionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_code):
            query['objectCode'] = request.object_code
        if not DaraCore.is_null(request.object_id):
            query['objectId'] = request.object_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableVersionDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableVersionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_variable_version_detail_with_options_async(
        self,
        request: main_models.DescribeVariableVersionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVariableVersionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_code):
            query['objectCode'] = request.object_code
        if not DaraCore.is_null(request.object_id):
            query['objectId'] = request.object_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVariableVersionDetail',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVariableVersionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_variable_version_detail(
        self,
        request: main_models.DescribeVariableVersionDetailRequest,
    ) -> main_models.DescribeVariableVersionDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_variable_version_detail_with_options(request, runtime)

    async def describe_variable_version_detail_async(
        self,
        request: main_models.DescribeVariableVersionDetailRequest,
    ) -> main_models.DescribeVariableVersionDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_variable_version_detail_with_options_async(request, runtime)

    def describe_version_page_list_with_options(
        self,
        request: main_models.DescribeVersionPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVersionPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.object_code):
            query['objectCode'] = request.object_code
        if not DaraCore.is_null(request.object_id):
            query['objectId'] = request.object_id
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.paging):
            query['paging'] = request.paging
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVersionPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVersionPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_version_page_list_with_options_async(
        self,
        request: main_models.DescribeVersionPageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVersionPageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.object_code):
            query['objectCode'] = request.object_code
        if not DaraCore.is_null(request.object_id):
            query['objectId'] = request.object_id
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.paging):
            query['paging'] = request.paging
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVersionPageList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVersionPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_version_page_list(
        self,
        request: main_models.DescribeVersionPageListRequest,
    ) -> main_models.DescribeVersionPageListResponse:
        runtime = RuntimeOptions()
        return self.describe_version_page_list_with_options(request, runtime)

    async def describe_version_page_list_async(
        self,
        request: main_models.DescribeVersionPageListRequest,
    ) -> main_models.DescribeVersionPageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_version_page_list_with_options_async(request, runtime)

    def download_smaple_batch_with_options(
        self,
        request: main_models.DownloadSmapleBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSmapleBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_uuid):
            query['batchUuid'] = request.batch_uuid
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadSmapleBatch',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSmapleBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_smaple_batch_with_options_async(
        self,
        request: main_models.DownloadSmapleBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSmapleBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_uuid):
            query['batchUuid'] = request.batch_uuid
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadSmapleBatch',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSmapleBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_smaple_batch(
        self,
        request: main_models.DownloadSmapleBatchRequest,
    ) -> main_models.DownloadSmapleBatchResponse:
        runtime = RuntimeOptions()
        return self.download_smaple_batch_with_options(request, runtime)

    async def download_smaple_batch_async(
        self,
        request: main_models.DownloadSmapleBatchRequest,
    ) -> main_models.DownloadSmapleBatchResponse:
        runtime = RuntimeOptions()
        return await self.download_smaple_batch_with_options_async(request, runtime)

    def expression_test_with_options(
        self,
        request: main_models.ExpressionTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExpressionTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.expression_variable_ids):
            query['expressionVariableIds'] = request.expression_variable_ids
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExpressionTest',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpressionTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def expression_test_with_options_async(
        self,
        request: main_models.ExpressionTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExpressionTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.expression_variable_ids):
            query['expressionVariableIds'] = request.expression_variable_ids
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExpressionTest',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpressionTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expression_test(
        self,
        request: main_models.ExpressionTestRequest,
    ) -> main_models.ExpressionTestResponse:
        runtime = RuntimeOptions()
        return self.expression_test_with_options(request, runtime)

    async def expression_test_async(
        self,
        request: main_models.ExpressionTestRequest,
    ) -> main_models.ExpressionTestResponse:
        runtime = RuntimeOptions()
        return await self.expression_test_with_options_async(request, runtime)

    def file_upload_with_options(
        self,
        request: main_models.FileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tab):
            query['Tab'] = request.tab
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FileUpload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def file_upload_with_options_async(
        self,
        request: main_models.FileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tab):
            query['Tab'] = request.tab
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FileUpload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def file_upload(
        self,
        request: main_models.FileUploadRequest,
    ) -> main_models.FileUploadResponse:
        runtime = RuntimeOptions()
        return self.file_upload_with_options(request, runtime)

    async def file_upload_async(
        self,
        request: main_models.FileUploadRequest,
    ) -> main_models.FileUploadResponse:
        runtime = RuntimeOptions()
        return await self.file_upload_with_options_async(request, runtime)

    def import_field_with_options(
        self,
        request: main_models.ImportFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_field_with_options_async(
        self,
        request: main_models.ImportFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_field(
        self,
        request: main_models.ImportFieldRequest,
    ) -> main_models.ImportFieldResponse:
        runtime = RuntimeOptions()
        return self.import_field_with_options(request, runtime)

    async def import_field_async(
        self,
        request: main_models.ImportFieldRequest,
    ) -> main_models.ImportFieldResponse:
        runtime = RuntimeOptions()
        return await self.import_field_with_options_async(request, runtime)

    def import_name_list_with_options(
        self,
        request: main_models.ImportNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.data):
            query['data'] = request.data
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.import_type):
            query['importType'] = request.import_type
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.name_list_type):
            query['nameListType'] = request.name_list_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_name_list_with_options_async(
        self,
        request: main_models.ImportNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.data):
            query['data'] = request.data
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.import_type):
            query['importType'] = request.import_type
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.name_list_type):
            query['nameListType'] = request.name_list_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportNameList',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_name_list(
        self,
        request: main_models.ImportNameListRequest,
    ) -> main_models.ImportNameListResponse:
        runtime = RuntimeOptions()
        return self.import_name_list_with_options(request, runtime)

    async def import_name_list_async(
        self,
        request: main_models.ImportNameListRequest,
    ) -> main_models.ImportNameListResponse:
        runtime = RuntimeOptions()
        return await self.import_name_list_with_options_async(request, runtime)

    def import_template_event_with_options(
        self,
        request: main_models.ImportTemplateEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportTemplateEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_template_ids):
            query['eventTemplateIds'] = request.event_template_ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportTemplateEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportTemplateEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_template_event_with_options_async(
        self,
        request: main_models.ImportTemplateEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportTemplateEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_template_ids):
            query['eventTemplateIds'] = request.event_template_ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportTemplateEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportTemplateEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_template_event(
        self,
        request: main_models.ImportTemplateEventRequest,
    ) -> main_models.ImportTemplateEventResponse:
        runtime = RuntimeOptions()
        return self.import_template_event_with_options(request, runtime)

    async def import_template_event_async(
        self,
        request: main_models.ImportTemplateEventRequest,
    ) -> main_models.ImportTemplateEventResponse:
        runtime = RuntimeOptions()
        return await self.import_template_event_with_options_async(request, runtime)

    def list_variable_define_with_options(
        self,
        request: main_models.ListVariableDefineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVariableDefineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.allow_bind):
            query['allowBind'] = request.allow_bind
        if not DaraCore.is_null(request.charging_mode):
            query['chargingMode'] = request.charging_mode
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.paging):
            query['paging'] = request.paging
        if not DaraCore.is_null(request.query_content):
            query['queryContent'] = request.query_content
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.role_type):
            query['roleType'] = request.role_type
        if not DaraCore.is_null(request.scenes_str):
            query['scenesStr'] = request.scenes_str
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.types_str):
            query['typesStr'] = request.types_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVariableDefine',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVariableDefineResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_variable_define_with_options_async(
        self,
        request: main_models.ListVariableDefineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVariableDefineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.allow_bind):
            query['allowBind'] = request.allow_bind
        if not DaraCore.is_null(request.charging_mode):
            query['chargingMode'] = request.charging_mode
        if not DaraCore.is_null(request.current_page):
            query['currentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.paging):
            query['paging'] = request.paging
        if not DaraCore.is_null(request.query_content):
            query['queryContent'] = request.query_content
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.role_type):
            query['roleType'] = request.role_type
        if not DaraCore.is_null(request.scenes_str):
            query['scenesStr'] = request.scenes_str
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        if not DaraCore.is_null(request.types_str):
            query['typesStr'] = request.types_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVariableDefine',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVariableDefineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_variable_define(
        self,
        request: main_models.ListVariableDefineRequest,
    ) -> main_models.ListVariableDefineResponse:
        runtime = RuntimeOptions()
        return self.list_variable_define_with_options(request, runtime)

    async def list_variable_define_async(
        self,
        request: main_models.ListVariableDefineRequest,
    ) -> main_models.ListVariableDefineResponse:
        runtime = RuntimeOptions()
        return await self.list_variable_define_with_options_async(request, runtime)

    def model_delete_with_options(
        self,
        request: main_models.ModelDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelDelete',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_delete_with_options_async(
        self,
        request: main_models.ModelDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelDelete',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_delete(
        self,
        request: main_models.ModelDeleteRequest,
    ) -> main_models.ModelDeleteResponse:
        runtime = RuntimeOptions()
        return self.model_delete_with_options(request, runtime)

    async def model_delete_async(
        self,
        request: main_models.ModelDeleteRequest,
    ) -> main_models.ModelDeleteResponse:
        runtime = RuntimeOptions()
        return await self.model_delete_with_options_async(request, runtime)

    def model_file_upload_with_options(
        self,
        request: main_models.ModelFileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelFileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_name):
            query['ObjectName'] = request.object_name
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelFileUpload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelFileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_file_upload_with_options_async(
        self,
        request: main_models.ModelFileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelFileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_name):
            query['ObjectName'] = request.object_name
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelFileUpload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelFileUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_file_upload(
        self,
        request: main_models.ModelFileUploadRequest,
    ) -> main_models.ModelFileUploadResponse:
        runtime = RuntimeOptions()
        return self.model_file_upload_with_options(request, runtime)

    async def model_file_upload_async(
        self,
        request: main_models.ModelFileUploadRequest,
    ) -> main_models.ModelFileUploadResponse:
        runtime = RuntimeOptions()
        return await self.model_file_upload_with_options_async(request, runtime)

    def model_is_using_with_options(
        self,
        request: main_models.ModelIsUsingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelIsUsingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_code):
            query['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelIsUsing',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelIsUsingResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_is_using_with_options_async(
        self,
        request: main_models.ModelIsUsingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelIsUsingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_code):
            query['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelIsUsing',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelIsUsingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_is_using(
        self,
        request: main_models.ModelIsUsingRequest,
    ) -> main_models.ModelIsUsingResponse:
        runtime = RuntimeOptions()
        return self.model_is_using_with_options(request, runtime)

    async def model_is_using_async(
        self,
        request: main_models.ModelIsUsingRequest,
    ) -> main_models.ModelIsUsingResponse:
        runtime = RuntimeOptions()
        return await self.model_is_using_with_options_async(request, runtime)

    def model_name_is_duplication_with_options(
        self,
        request: main_models.ModelNameIsDuplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelNameIsDuplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelNameIsDuplication',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelNameIsDuplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_name_is_duplication_with_options_async(
        self,
        request: main_models.ModelNameIsDuplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelNameIsDuplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelNameIsDuplication',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelNameIsDuplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_name_is_duplication(
        self,
        request: main_models.ModelNameIsDuplicationRequest,
    ) -> main_models.ModelNameIsDuplicationResponse:
        runtime = RuntimeOptions()
        return self.model_name_is_duplication_with_options(request, runtime)

    async def model_name_is_duplication_async(
        self,
        request: main_models.ModelNameIsDuplicationRequest,
    ) -> main_models.ModelNameIsDuplicationResponse:
        runtime = RuntimeOptions()
        return await self.model_name_is_duplication_with_options_async(request, runtime)

    def model_sample_download_with_options(
        self,
        request: main_models.ModelSampleDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelSampleDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelSampleDownload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelSampleDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_sample_download_with_options_async(
        self,
        request: main_models.ModelSampleDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModelSampleDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelSampleDownload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelSampleDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_sample_download(
        self,
        request: main_models.ModelSampleDownloadRequest,
    ) -> main_models.ModelSampleDownloadResponse:
        runtime = RuntimeOptions()
        return self.model_sample_download_with_options(request, runtime)

    async def model_sample_download_async(
        self,
        request: main_models.ModelSampleDownloadRequest,
    ) -> main_models.ModelSampleDownloadResponse:
        runtime = RuntimeOptions()
        return await self.model_sample_download_with_options_async(request, runtime)

    def modify_app_key_with_options(
        self,
        request: main_models.ModifyAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.app_key):
            query['appKey'] = request.app_key
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppKey',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_key_with_options_async(
        self,
        request: main_models.ModifyAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.app_key):
            query['appKey'] = request.app_key
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppKey',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_key(
        self,
        request: main_models.ModifyAppKeyRequest,
    ) -> main_models.ModifyAppKeyResponse:
        runtime = RuntimeOptions()
        return self.modify_app_key_with_options(request, runtime)

    async def modify_app_key_async(
        self,
        request: main_models.ModifyAppKeyRequest,
    ) -> main_models.ModifyAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_key_with_options_async(request, runtime)

    def modify_cust_variable_with_options(
        self,
        request: main_models.ModifyCustVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cust_variable_with_options_async(
        self,
        request: main_models.ModifyCustVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cust_variable(
        self,
        request: main_models.ModifyCustVariableRequest,
    ) -> main_models.ModifyCustVariableResponse:
        runtime = RuntimeOptions()
        return self.modify_cust_variable_with_options(request, runtime)

    async def modify_cust_variable_async(
        self,
        request: main_models.ModifyCustVariableRequest,
    ) -> main_models.ModifyCustVariableResponse:
        runtime = RuntimeOptions()
        return await self.modify_cust_variable_with_options_async(request, runtime)

    def modify_event_with_options(
        self,
        request: main_models.ModifyEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.biz_version):
            query['bizVersion'] = request.biz_version
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.input_fields_str):
            query['inputFieldsStr'] = request.input_fields_str
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_event_with_options_async(
        self,
        request: main_models.ModifyEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.biz_version):
            query['bizVersion'] = request.biz_version
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.input_fields_str):
            query['inputFieldsStr'] = request.input_fields_str
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_event(
        self,
        request: main_models.ModifyEventRequest,
    ) -> main_models.ModifyEventResponse:
        runtime = RuntimeOptions()
        return self.modify_event_with_options(request, runtime)

    async def modify_event_async(
        self,
        request: main_models.ModifyEventRequest,
    ) -> main_models.ModifyEventResponse:
        runtime = RuntimeOptions()
        return await self.modify_event_with_options_async(request, runtime)

    def modify_event_status_with_options(
        self,
        request: main_models.ModifyEventStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEventStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.from_event_satus):
            query['fromEventSatus'] = request.from_event_satus
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.to_event_satus):
            query['toEventSatus'] = request.to_event_satus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEventStatus',
            version = '2021-09-10',
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
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.from_event_satus):
            query['fromEventSatus'] = request.from_event_satus
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.to_event_satus):
            query['toEventSatus'] = request.to_event_satus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEventStatus',
            version = '2021-09-10',
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

    def modify_expression_variable_with_options(
        self,
        request: main_models.ModifyExpressionVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressionVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.outlier):
            query['outlier'] = request.outlier
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressionVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressionVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_expression_variable_with_options_async(
        self,
        request: main_models.ModifyExpressionVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressionVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.outlier):
            query['outlier'] = request.outlier
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressionVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressionVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_expression_variable(
        self,
        request: main_models.ModifyExpressionVariableRequest,
    ) -> main_models.ModifyExpressionVariableResponse:
        runtime = RuntimeOptions()
        return self.modify_expression_variable_with_options(request, runtime)

    async def modify_expression_variable_async(
        self,
        request: main_models.ModifyExpressionVariableRequest,
    ) -> main_models.ModifyExpressionVariableResponse:
        runtime = RuntimeOptions()
        return await self.modify_expression_variable_with_options_async(request, runtime)

    def modify_field_with_options(
        self,
        request: main_models.ModifyFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.classify):
            query['classify'] = request.classify
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.enum_data):
            query['enumData'] = request.enum_data
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_field_with_options_async(
        self,
        request: main_models.ModifyFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.classify):
            query['classify'] = request.classify
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.enum_data):
            query['enumData'] = request.enum_data
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_field(
        self,
        request: main_models.ModifyFieldRequest,
    ) -> main_models.ModifyFieldResponse:
        runtime = RuntimeOptions()
        return self.modify_field_with_options(request, runtime)

    async def modify_field_async(
        self,
        request: main_models.ModifyFieldRequest,
    ) -> main_models.ModifyFieldResponse:
        runtime = RuntimeOptions()
        return await self.modify_field_with_options_async(request, runtime)

    def modify_rule_priority_with_options(
        self,
        request: main_models.ModifyRulePriorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRulePriorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.priority):
            query['priority'] = request.priority
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRulePriority',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRulePriorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_priority_with_options_async(
        self,
        request: main_models.ModifyRulePriorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRulePriorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.priority):
            query['priority'] = request.priority
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRulePriority',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRulePriorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rule_priority(
        self,
        request: main_models.ModifyRulePriorityRequest,
    ) -> main_models.ModifyRulePriorityResponse:
        runtime = RuntimeOptions()
        return self.modify_rule_priority_with_options(request, runtime)

    async def modify_rule_priority_async(
        self,
        request: main_models.ModifyRulePriorityRequest,
    ) -> main_models.ModifyRulePriorityResponse:
        runtime = RuntimeOptions()
        return await self.modify_rule_priority_with_options_async(request, runtime)

    def modify_rule_status_with_options(
        self,
        request: main_models.ModifyRuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.apply_user_id):
            query['applyUserId'] = request.apply_user_id
        if not DaraCore.is_null(request.apply_user_name):
            query['applyUserName'] = request.apply_user_name
        if not DaraCore.is_null(request.audit_remark):
            query['auditRemark'] = request.audit_remark
        if not DaraCore.is_null(request.audit_user_id):
            query['auditUserId'] = request.audit_user_id
        if not DaraCore.is_null(request.audit_user_name):
            query['auditUserName'] = request.audit_user_name
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.event_type):
            query['eventType'] = request.event_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_audit_type):
            query['ruleAuditType'] = request.rule_audit_type
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRuleStatus',
            version = '2021-09-10',
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
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.apply_user_id):
            query['applyUserId'] = request.apply_user_id
        if not DaraCore.is_null(request.apply_user_name):
            query['applyUserName'] = request.apply_user_name
        if not DaraCore.is_null(request.audit_remark):
            query['auditRemark'] = request.audit_remark
        if not DaraCore.is_null(request.audit_user_id):
            query['auditUserId'] = request.audit_user_id
        if not DaraCore.is_null(request.audit_user_name):
            query['auditUserName'] = request.audit_user_name
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.event_type):
            query['eventType'] = request.event_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_audit_type):
            query['ruleAuditType'] = request.rule_audit_type
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRuleStatus',
            version = '2021-09-10',
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

    def open_console_sls_with_options(
        self,
        request: main_models.OpenConsoleSlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenConsoleSlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenConsoleSls',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenConsoleSlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_console_sls_with_options_async(
        self,
        request: main_models.OpenConsoleSlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenConsoleSlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.scene):
            query['scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenConsoleSls',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenConsoleSlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_console_sls(
        self,
        request: main_models.OpenConsoleSlsRequest,
    ) -> main_models.OpenConsoleSlsResponse:
        runtime = RuntimeOptions()
        return self.open_console_sls_with_options(request, runtime)

    async def open_console_sls_async(
        self,
        request: main_models.OpenConsoleSlsRequest,
    ) -> main_models.OpenConsoleSlsResponse:
        runtime = RuntimeOptions()
        return await self.open_console_sls_with_options_async(request, runtime)

    def operate_favorite_variable_with_options(
        self,
        request: main_models.OperateFavoriteVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateFavoriteVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.operate):
            query['operate'] = request.operate
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateFavoriteVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateFavoriteVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_favorite_variable_with_options_async(
        self,
        request: main_models.OperateFavoriteVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateFavoriteVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.operate):
            query['operate'] = request.operate
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateFavoriteVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateFavoriteVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_favorite_variable(
        self,
        request: main_models.OperateFavoriteVariableRequest,
    ) -> main_models.OperateFavoriteVariableResponse:
        runtime = RuntimeOptions()
        return self.operate_favorite_variable_with_options(request, runtime)

    async def operate_favorite_variable_async(
        self,
        request: main_models.OperateFavoriteVariableRequest,
    ) -> main_models.OperateFavoriteVariableResponse:
        runtime = RuntimeOptions()
        return await self.operate_favorite_variable_with_options_async(request, runtime)

    def permission_check_with_options(
        self,
        request: main_models.PermissionCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PermissionCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PermissionCheck',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PermissionCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def permission_check_with_options_async(
        self,
        request: main_models.PermissionCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PermissionCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PermissionCheck',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PermissionCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def permission_check(
        self,
        request: main_models.PermissionCheckRequest,
    ) -> main_models.PermissionCheckResponse:
        runtime = RuntimeOptions()
        return self.permission_check_with_options(request, runtime)

    async def permission_check_async(
        self,
        request: main_models.PermissionCheckRequest,
    ) -> main_models.PermissionCheckResponse:
        runtime = RuntimeOptions()
        return await self.permission_check_with_options_async(request, runtime)

    def poc_create_task_with_options(
        self,
        request: main_models.PocCreateTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PocCreateTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date_format):
            query['DateFormat'] = request.date_format
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PocCreateTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PocCreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def poc_create_task_with_options_async(
        self,
        request: main_models.PocCreateTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PocCreateTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date_format):
            query['DateFormat'] = request.date_format
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PocCreateTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PocCreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poc_create_task(
        self,
        request: main_models.PocCreateTaskRequest,
    ) -> main_models.PocCreateTaskResponse:
        runtime = RuntimeOptions()
        return self.poc_create_task_with_options(request, runtime)

    async def poc_create_task_async(
        self,
        request: main_models.PocCreateTaskRequest,
    ) -> main_models.PocCreateTaskResponse:
        runtime = RuntimeOptions()
        return await self.poc_create_task_with_options_async(request, runtime)

    def poc_get_download_url_with_options(
        self,
        request: main_models.PocGetDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PocGetDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PocGetDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PocGetDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def poc_get_download_url_with_options_async(
        self,
        request: main_models.PocGetDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PocGetDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PocGetDownloadUrl',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PocGetDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poc_get_download_url(
        self,
        request: main_models.PocGetDownloadUrlRequest,
    ) -> main_models.PocGetDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.poc_get_download_url_with_options(request, runtime)

    async def poc_get_download_url_async(
        self,
        request: main_models.PocGetDownloadUrlRequest,
    ) -> main_models.PocGetDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.poc_get_download_url_with_options_async(request, runtime)

    def poc_get_token_with_options(
        self,
        request: main_models.PocGetTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PocGetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PocGetToken',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PocGetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def poc_get_token_with_options_async(
        self,
        request: main_models.PocGetTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PocGetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PocGetToken',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PocGetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poc_get_token(
        self,
        request: main_models.PocGetTokenRequest,
    ) -> main_models.PocGetTokenResponse:
        runtime = RuntimeOptions()
        return self.poc_get_token_with_options(request, runtime)

    async def poc_get_token_async(
        self,
        request: main_models.PocGetTokenRequest,
    ) -> main_models.PocGetTokenResponse:
        runtime = RuntimeOptions()
        return await self.poc_get_token_with_options_async(request, runtime)

    def poc_send_data_with_options(
        self,
        request: main_models.PocSendDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PocSendDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_no):
            query['BatchNo'] = request.batch_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.params_list):
            query['ParamsList'] = request.params_list
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PocSendData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PocSendDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def poc_send_data_with_options_async(
        self,
        request: main_models.PocSendDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PocSendDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_no):
            query['BatchNo'] = request.batch_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.params_list):
            query['ParamsList'] = request.params_list
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PocSendData',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PocSendDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poc_send_data(
        self,
        request: main_models.PocSendDataRequest,
    ) -> main_models.PocSendDataResponse:
        runtime = RuntimeOptions()
        return self.poc_send_data_with_options(request, runtime)

    async def poc_send_data_async(
        self,
        request: main_models.PocSendDataRequest,
    ) -> main_models.PocSendDataResponse:
        runtime = RuntimeOptions()
        return await self.poc_send_data_with_options_async(request, runtime)

    def query_auth_rule_detail_by_rule_id_with_options(
        self,
        request: main_models.QueryAuthRuleDetailByRuleIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuthRuleDetailByRuleIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuthRuleDetailByRuleId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuthRuleDetailByRuleIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_auth_rule_detail_by_rule_id_with_options_async(
        self,
        request: main_models.QueryAuthRuleDetailByRuleIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuthRuleDetailByRuleIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuthRuleDetailByRuleId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuthRuleDetailByRuleIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_auth_rule_detail_by_rule_id(
        self,
        request: main_models.QueryAuthRuleDetailByRuleIdRequest,
    ) -> main_models.QueryAuthRuleDetailByRuleIdResponse:
        runtime = RuntimeOptions()
        return self.query_auth_rule_detail_by_rule_id_with_options(request, runtime)

    async def query_auth_rule_detail_by_rule_id_async(
        self,
        request: main_models.QueryAuthRuleDetailByRuleIdRequest,
    ) -> main_models.QueryAuthRuleDetailByRuleIdResponse:
        runtime = RuntimeOptions()
        return await self.query_auth_rule_detail_by_rule_id_with_options_async(request, runtime)

    def recall_rule_audit_with_options(
        self,
        request: main_models.RecallRuleAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecallRuleAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecallRuleAudit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecallRuleAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def recall_rule_audit_with_options_async(
        self,
        request: main_models.RecallRuleAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecallRuleAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecallRuleAudit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecallRuleAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recall_rule_audit(
        self,
        request: main_models.RecallRuleAuditRequest,
    ) -> main_models.RecallRuleAuditResponse:
        runtime = RuntimeOptions()
        return self.recall_rule_audit_with_options(request, runtime)

    async def recall_rule_audit_async(
        self,
        request: main_models.RecallRuleAuditRequest,
    ) -> main_models.RecallRuleAuditResponse:
        runtime = RuntimeOptions()
        return await self.recall_rule_audit_with_options_async(request, runtime)

    def remove_event_with_options(
        self,
        request: main_models.RemoveEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_code):
            query['templateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_event_with_options_async(
        self,
        request: main_models.RemoveEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.create_type):
            query['createType'] = request.create_type
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.template_code):
            query['templateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_event(
        self,
        request: main_models.RemoveEventRequest,
    ) -> main_models.RemoveEventResponse:
        runtime = RuntimeOptions()
        return self.remove_event_with_options(request, runtime)

    async def remove_event_async(
        self,
        request: main_models.RemoveEventRequest,
    ) -> main_models.RemoveEventResponse:
        runtime = RuntimeOptions()
        return await self.remove_event_with_options_async(request, runtime)

    def sample_file_download_with_options(
        self,
        request: main_models.SampleFileDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SampleFileDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.tab):
            query['Tab'] = request.tab
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SampleFileDownload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SampleFileDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def sample_file_download_with_options_async(
        self,
        request: main_models.SampleFileDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SampleFileDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.tab):
            query['Tab'] = request.tab
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SampleFileDownload',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SampleFileDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sample_file_download(
        self,
        request: main_models.SampleFileDownloadRequest,
    ) -> main_models.SampleFileDownloadResponse:
        runtime = RuntimeOptions()
        return self.sample_file_download_with_options(request, runtime)

    async def sample_file_download_async(
        self,
        request: main_models.SampleFileDownloadRequest,
    ) -> main_models.SampleFileDownloadResponse:
        runtime = RuntimeOptions()
        return await self.sample_file_download_with_options_async(request, runtime)

    def save_analysis_column_with_options(
        self,
        request: main_models.SaveAnalysisColumnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAnalysisColumnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.columns):
            query['columns'] = request.columns
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAnalysisColumn',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAnalysisColumnResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_analysis_column_with_options_async(
        self,
        request: main_models.SaveAnalysisColumnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveAnalysisColumnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.columns):
            query['columns'] = request.columns
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveAnalysisColumn',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAnalysisColumnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_analysis_column(
        self,
        request: main_models.SaveAnalysisColumnRequest,
    ) -> main_models.SaveAnalysisColumnResponse:
        runtime = RuntimeOptions()
        return self.save_analysis_column_with_options(request, runtime)

    async def save_analysis_column_async(
        self,
        request: main_models.SaveAnalysisColumnRequest,
    ) -> main_models.SaveAnalysisColumnResponse:
        runtime = RuntimeOptions()
        return await self.save_analysis_column_with_options_async(request, runtime)

    def save_by_pass_or_shunt_event_with_options(
        self,
        request: main_models.SaveByPassOrShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveByPassOrShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.event_type):
            query['eventType'] = request.event_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveByPassOrShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveByPassOrShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_by_pass_or_shunt_event_with_options_async(
        self,
        request: main_models.SaveByPassOrShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveByPassOrShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.event_type):
            query['eventType'] = request.event_type
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveByPassOrShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveByPassOrShuntEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_by_pass_or_shunt_event(
        self,
        request: main_models.SaveByPassOrShuntEventRequest,
    ) -> main_models.SaveByPassOrShuntEventResponse:
        runtime = RuntimeOptions()
        return self.save_by_pass_or_shunt_event_with_options(request, runtime)

    async def save_by_pass_or_shunt_event_async(
        self,
        request: main_models.SaveByPassOrShuntEventRequest,
    ) -> main_models.SaveByPassOrShuntEventResponse:
        runtime = RuntimeOptions()
        return await self.save_by_pass_or_shunt_event_with_options_async(request, runtime)

    def start_or_stop_by_pass_shunt_event_with_options(
        self,
        request: main_models.StartOrStopByPassShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartOrStopByPassShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartOrStopByPassShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartOrStopByPassShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_or_stop_by_pass_shunt_event_with_options_async(
        self,
        request: main_models.StartOrStopByPassShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartOrStopByPassShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartOrStopByPassShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartOrStopByPassShuntEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_or_stop_by_pass_shunt_event(
        self,
        request: main_models.StartOrStopByPassShuntEventRequest,
    ) -> main_models.StartOrStopByPassShuntEventResponse:
        runtime = RuntimeOptions()
        return self.start_or_stop_by_pass_shunt_event_with_options(request, runtime)

    async def start_or_stop_by_pass_shunt_event_async(
        self,
        request: main_models.StartOrStopByPassShuntEventRequest,
    ) -> main_models.StartOrStopByPassShuntEventResponse:
        runtime = RuntimeOptions()
        return await self.start_or_stop_by_pass_shunt_event_with_options_async(request, runtime)

    def start_simulation_task_with_options(
        self,
        request: main_models.StartSimulationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSimulationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartSimulationTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSimulationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_simulation_task_with_options_async(
        self,
        request: main_models.StartSimulationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSimulationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartSimulationTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSimulationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_simulation_task(
        self,
        request: main_models.StartSimulationTaskRequest,
    ) -> main_models.StartSimulationTaskResponse:
        runtime = RuntimeOptions()
        return self.start_simulation_task_with_options(request, runtime)

    async def start_simulation_task_async(
        self,
        request: main_models.StartSimulationTaskRequest,
    ) -> main_models.StartSimulationTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_simulation_task_with_options_async(request, runtime)

    def stop_simulation_task_with_options(
        self,
        request: main_models.StopSimulationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopSimulationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopSimulationTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSimulationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_simulation_task_with_options_async(
        self,
        request: main_models.StopSimulationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopSimulationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopSimulationTask',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSimulationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_simulation_task(
        self,
        request: main_models.StopSimulationTaskRequest,
    ) -> main_models.StopSimulationTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_simulation_task_with_options(request, runtime)

    async def stop_simulation_task_async(
        self,
        request: main_models.StopSimulationTaskRequest,
    ) -> main_models.StopSimulationTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_simulation_task_with_options_async(request, runtime)

    def switch_expression_variable_with_options(
        self,
        request: main_models.SwitchExpressionVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchExpressionVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchExpressionVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchExpressionVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_expression_variable_with_options_async(
        self,
        request: main_models.SwitchExpressionVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchExpressionVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchExpressionVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchExpressionVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_expression_variable(
        self,
        request: main_models.SwitchExpressionVariableRequest,
    ) -> main_models.SwitchExpressionVariableResponse:
        runtime = RuntimeOptions()
        return self.switch_expression_variable_with_options(request, runtime)

    async def switch_expression_variable_async(
        self,
        request: main_models.SwitchExpressionVariableRequest,
    ) -> main_models.SwitchExpressionVariableResponse:
        runtime = RuntimeOptions()
        return await self.switch_expression_variable_with_options_async(request, runtime)

    def switch_field_with_options(
        self,
        request: main_models.SwitchFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_field_with_options_async(
        self,
        request: main_models.SwitchFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchField',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_field(
        self,
        request: main_models.SwitchFieldRequest,
    ) -> main_models.SwitchFieldResponse:
        runtime = RuntimeOptions()
        return self.switch_field_with_options(request, runtime)

    async def switch_field_async(
        self,
        request: main_models.SwitchFieldRequest,
    ) -> main_models.SwitchFieldResponse:
        runtime = RuntimeOptions()
        return await self.switch_field_with_options_async(request, runtime)

    def switch_query_variable_with_options(
        self,
        request: main_models.SwitchQueryVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchQueryVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchQueryVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchQueryVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_query_variable_with_options_async(
        self,
        request: main_models.SwitchQueryVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchQueryVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchQueryVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchQueryVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_query_variable(
        self,
        request: main_models.SwitchQueryVariableRequest,
    ) -> main_models.SwitchQueryVariableResponse:
        runtime = RuntimeOptions()
        return self.switch_query_variable_with_options(request, runtime)

    async def switch_query_variable_async(
        self,
        request: main_models.SwitchQueryVariableRequest,
    ) -> main_models.SwitchQueryVariableResponse:
        runtime = RuntimeOptions()
        return await self.switch_query_variable_with_options_async(request, runtime)

    def switch_to_online_with_options(
        self,
        request: main_models.SwitchToOnlineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchToOnlineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchToOnline',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchToOnlineResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_to_online_with_options_async(
        self,
        request: main_models.SwitchToOnlineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchToOnlineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchToOnline',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchToOnlineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_to_online(
        self,
        request: main_models.SwitchToOnlineRequest,
    ) -> main_models.SwitchToOnlineResponse:
        runtime = RuntimeOptions()
        return self.switch_to_online_with_options(request, runtime)

    async def switch_to_online_async(
        self,
        request: main_models.SwitchToOnlineRequest,
    ) -> main_models.SwitchToOnlineResponse:
        runtime = RuntimeOptions()
        return await self.switch_to_online_with_options_async(request, runtime)

    def switch_variable_with_options(
        self,
        request: main_models.SwitchVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_variable_with_options_async(
        self,
        request: main_models.SwitchVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_version):
            query['dataVersion'] = request.data_version
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_variable(
        self,
        request: main_models.SwitchVariableRequest,
    ) -> main_models.SwitchVariableResponse:
        runtime = RuntimeOptions()
        return self.switch_variable_with_options(request, runtime)

    async def switch_variable_async(
        self,
        request: main_models.SwitchVariableRequest,
    ) -> main_models.SwitchVariableResponse:
        runtime = RuntimeOptions()
        return await self.switch_variable_with_options_async(request, runtime)

    def task_name_by_user_id_with_options(
        self,
        request: main_models.TaskNameByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskNameByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskNameByUserId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskNameByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_name_by_user_id_with_options_async(
        self,
        request: main_models.TaskNameByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TaskNameByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_id):
            query['RegId'] = request.reg_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TaskNameByUserId',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TaskNameByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_name_by_user_id(
        self,
        request: main_models.TaskNameByUserIdRequest,
    ) -> main_models.TaskNameByUserIdResponse:
        runtime = RuntimeOptions()
        return self.task_name_by_user_id_with_options(request, runtime)

    async def task_name_by_user_id_async(
        self,
        request: main_models.TaskNameByUserIdRequest,
    ) -> main_models.TaskNameByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.task_name_by_user_id_with_options_async(request, runtime)

    def update_analysis_condition_favorite_with_options(
        self,
        request: main_models.UpdateAnalysisConditionFavoriteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAnalysisConditionFavoriteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAnalysisConditionFavorite',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAnalysisConditionFavoriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_analysis_condition_favorite_with_options_async(
        self,
        request: main_models.UpdateAnalysisConditionFavoriteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAnalysisConditionFavoriteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.condition):
            query['condition'] = request.condition
        if not DaraCore.is_null(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not DaraCore.is_null(request.field_name):
            query['fieldName'] = request.field_name
        if not DaraCore.is_null(request.field_value):
            query['fieldValue'] = request.field_value
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAnalysisConditionFavorite',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAnalysisConditionFavoriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_analysis_condition_favorite(
        self,
        request: main_models.UpdateAnalysisConditionFavoriteRequest,
    ) -> main_models.UpdateAnalysisConditionFavoriteResponse:
        runtime = RuntimeOptions()
        return self.update_analysis_condition_favorite_with_options(request, runtime)

    async def update_analysis_condition_favorite_async(
        self,
        request: main_models.UpdateAnalysisConditionFavoriteRequest,
    ) -> main_models.UpdateAnalysisConditionFavoriteResponse:
        runtime = RuntimeOptions()
        return await self.update_analysis_condition_favorite_with_options_async(request, runtime)

    def update_audit_with_options(
        self,
        request: main_models.UpdateAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.audit_msg):
            query['auditMsg'] = request.audit_msg
        if not DaraCore.is_null(request.audit_relation_type):
            query['auditRelationType'] = request.audit_relation_type
        if not DaraCore.is_null(request.audit_status):
            query['auditStatus'] = request.audit_status
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAudit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_audit_with_options_async(
        self,
        request: main_models.UpdateAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.audit_msg):
            query['auditMsg'] = request.audit_msg
        if not DaraCore.is_null(request.audit_relation_type):
            query['auditRelationType'] = request.audit_relation_type
        if not DaraCore.is_null(request.audit_status):
            query['auditStatus'] = request.audit_status
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAudit',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_audit(
        self,
        request: main_models.UpdateAuditRequest,
    ) -> main_models.UpdateAuditResponse:
        runtime = RuntimeOptions()
        return self.update_audit_with_options(request, runtime)

    async def update_audit_async(
        self,
        request: main_models.UpdateAuditRequest,
    ) -> main_models.UpdateAuditResponse:
        runtime = RuntimeOptions()
        return await self.update_audit_with_options_async(request, runtime)

    def update_auth_rule_with_options(
        self,
        request: main_models.UpdateAuthRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuthRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAuthRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuthRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auth_rule_with_options_async(
        self,
        request: main_models.UpdateAuthRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuthRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAuthRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuthRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auth_rule(
        self,
        request: main_models.UpdateAuthRuleRequest,
    ) -> main_models.UpdateAuthRuleResponse:
        runtime = RuntimeOptions()
        return self.update_auth_rule_with_options(request, runtime)

    async def update_auth_rule_async(
        self,
        request: main_models.UpdateAuthRuleRequest,
    ) -> main_models.UpdateAuthRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_auth_rule_with_options_async(request, runtime)

    def update_by_pass_shunt_event_with_options(
        self,
        request: main_models.UpdateByPassShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateByPassShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateByPassShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateByPassShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_by_pass_shunt_event_with_options_async(
        self,
        request: main_models.UpdateByPassShuntEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateByPassShuntEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.event_id):
            query['eventId'] = request.event_id
        if not DaraCore.is_null(request.event_name):
            query['eventName'] = request.event_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateByPassShuntEvent',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateByPassShuntEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_by_pass_shunt_event(
        self,
        request: main_models.UpdateByPassShuntEventRequest,
    ) -> main_models.UpdateByPassShuntEventResponse:
        runtime = RuntimeOptions()
        return self.update_by_pass_shunt_event_with_options(request, runtime)

    async def update_by_pass_shunt_event_async(
        self,
        request: main_models.UpdateByPassShuntEventRequest,
    ) -> main_models.UpdateByPassShuntEventResponse:
        runtime = RuntimeOptions()
        return await self.update_by_pass_shunt_event_with_options_async(request, runtime)

    def update_data_source_with_options(
        self,
        request: main_models.UpdateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.oss_key):
            query['ossKey'] = request.oss_key
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSource',
            version = '2021-09-10',
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
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.oss_key):
            query['ossKey'] = request.oss_key
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSource',
            version = '2021-09-10',
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

    def update_query_variable_with_options(
        self,
        request: main_models.UpdateQueryVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQueryVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.outlier):
            query['outlier'] = request.outlier
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQueryVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQueryVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_query_variable_with_options_async(
        self,
        request: main_models.UpdateQueryVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQueryVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.expression):
            query['expression'] = request.expression
        if not DaraCore.is_null(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not DaraCore.is_null(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not DaraCore.is_null(request.id):
            query['id'] = request.id
        if not DaraCore.is_null(request.outlier):
            query['outlier'] = request.outlier
        if not DaraCore.is_null(request.outputs):
            query['outputs'] = request.outputs
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQueryVariable',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQueryVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_query_variable(
        self,
        request: main_models.UpdateQueryVariableRequest,
    ) -> main_models.UpdateQueryVariableResponse:
        runtime = RuntimeOptions()
        return self.update_query_variable_with_options(request, runtime)

    async def update_query_variable_async(
        self,
        request: main_models.UpdateQueryVariableRequest,
    ) -> main_models.UpdateQueryVariableResponse:
        runtime = RuntimeOptions()
        return await self.update_query_variable_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: main_models.UpdateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.logic_expression):
            query['logicExpression'] = request.logic_expression
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_body):
            query['ruleBody'] = request.rule_body
        if not DaraCore.is_null(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['ruleType'] = request.rule_type
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: main_models.UpdateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.logic_expression):
            query['logicExpression'] = request.logic_expression
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_body):
            query['ruleBody'] = request.rule_body
        if not DaraCore.is_null(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['ruleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['ruleType'] = request.rule_type
        if not DaraCore.is_null(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRule',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule(
        self,
        request: main_models.UpdateRuleRequest,
    ) -> main_models.UpdateRuleResponse:
        runtime = RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: main_models.UpdateRuleRequest,
    ) -> main_models.UpdateRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)

    def update_rule_base_with_options(
        self,
        request: main_models.UpdateRuleBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleBase',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_base_with_options_async(
        self,
        request: main_models.UpdateRuleBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not DaraCore.is_null(request.event_code):
            query['eventCode'] = request.event_code
        if not DaraCore.is_null(request.memo):
            query['memo'] = request.memo
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.rule_id):
            query['ruleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleBase',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_base(
        self,
        request: main_models.UpdateRuleBaseRequest,
    ) -> main_models.UpdateRuleBaseResponse:
        runtime = RuntimeOptions()
        return self.update_rule_base_with_options(request, runtime)

    async def update_rule_base_async(
        self,
        request: main_models.UpdateRuleBaseRequest,
    ) -> main_models.UpdateRuleBaseResponse:
        runtime = RuntimeOptions()
        return await self.update_rule_base_with_options_async(request, runtime)

    def update_sample_batch_with_options(
        self,
        request: main_models.UpdateSampleBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSampleBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.ids):
            query['ids'] = request.ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        if not DaraCore.is_null(request.versions):
            query['versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSampleBatch',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSampleBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sample_batch_with_options_async(
        self,
        request: main_models.UpdateSampleBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSampleBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.ids):
            query['ids'] = request.ids
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        if not DaraCore.is_null(request.versions):
            query['versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSampleBatch',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSampleBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sample_batch(
        self,
        request: main_models.UpdateSampleBatchRequest,
    ) -> main_models.UpdateSampleBatchResponse:
        runtime = RuntimeOptions()
        return self.update_sample_batch_with_options(request, runtime)

    async def update_sample_batch_async(
        self,
        request: main_models.UpdateSampleBatchRequest,
    ) -> main_models.UpdateSampleBatchResponse:
        runtime = RuntimeOptions()
        return await self.update_sample_batch_with_options_async(request, runtime)

    def upload_file_check_with_options(
        self,
        request: main_models.UploadFileCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadFileCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_name):
            query['batchName'] = request.batch_name
        if not DaraCore.is_null(request.data_type):
            query['dataType'] = request.data_type
        if not DaraCore.is_null(request.oss_file_name):
            query['ossFileName'] = request.oss_file_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_tag_type):
            query['sampleTagType'] = request.sample_tag_type
        if not DaraCore.is_null(request.service_list):
            query['serviceList'] = request.service_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadFileCheck',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadFileCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_file_check_with_options_async(
        self,
        request: main_models.UploadFileCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadFileCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.batch_name):
            query['batchName'] = request.batch_name
        if not DaraCore.is_null(request.data_type):
            query['dataType'] = request.data_type
        if not DaraCore.is_null(request.oss_file_name):
            query['ossFileName'] = request.oss_file_name
        if not DaraCore.is_null(request.reg_id):
            query['regId'] = request.reg_id
        if not DaraCore.is_null(request.sample_tag_type):
            query['sampleTagType'] = request.sample_tag_type
        if not DaraCore.is_null(request.service_list):
            query['serviceList'] = request.service_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadFileCheck',
            version = '2021-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadFileCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_file_check(
        self,
        request: main_models.UploadFileCheckRequest,
    ) -> main_models.UploadFileCheckResponse:
        runtime = RuntimeOptions()
        return self.upload_file_check_with_options(request, runtime)

    async def upload_file_check_async(
        self,
        request: main_models.UploadFileCheckRequest,
    ) -> main_models.UploadFileCheckResponse:
        runtime = RuntimeOptions()
        return await self.upload_file_check_with_options_async(request, runtime)
