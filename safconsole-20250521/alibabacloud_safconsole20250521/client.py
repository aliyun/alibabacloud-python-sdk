# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_safconsole20250521 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('safconsole', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_customer_module_basic_info_with_options(
        self,
        request: main_models.CreateCustomerModuleBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomerModuleBasicInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_name):
            query['CustomerModuleName'] = request.customer_module_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.module_type):
            query['ModuleType'] = request.module_type
        if not DaraCore.is_null(request.store_path):
            query['StorePath'] = request.store_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomerModuleBasicInfo',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomerModuleBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customer_module_basic_info_with_options_async(
        self,
        request: main_models.CreateCustomerModuleBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomerModuleBasicInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_name):
            query['CustomerModuleName'] = request.customer_module_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.module_type):
            query['ModuleType'] = request.module_type
        if not DaraCore.is_null(request.store_path):
            query['StorePath'] = request.store_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomerModuleBasicInfo',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomerModuleBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customer_module_basic_info(
        self,
        request: main_models.CreateCustomerModuleBasicInfoRequest,
    ) -> main_models.CreateCustomerModuleBasicInfoResponse:
        runtime = RuntimeOptions()
        return self.create_customer_module_basic_info_with_options(request, runtime)

    async def create_customer_module_basic_info_async(
        self,
        request: main_models.CreateCustomerModuleBasicInfoRequest,
    ) -> main_models.CreateCustomerModuleBasicInfoResponse:
        runtime = RuntimeOptions()
        return await self.create_customer_module_basic_info_with_options_async(request, runtime)

    def create_customer_module_meta_info_with_options(
        self,
        request: main_models.CreateCustomerModuleMetaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomerModuleMetaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        if not DaraCore.is_null(request.feature_string):
            query['FeatureString'] = request.feature_string
        if not DaraCore.is_null(request.feature_template):
            query['FeatureTemplate'] = request.feature_template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomerModuleMetaInfo',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomerModuleMetaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customer_module_meta_info_with_options_async(
        self,
        request: main_models.CreateCustomerModuleMetaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomerModuleMetaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        if not DaraCore.is_null(request.feature_string):
            query['FeatureString'] = request.feature_string
        if not DaraCore.is_null(request.feature_template):
            query['FeatureTemplate'] = request.feature_template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomerModuleMetaInfo',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomerModuleMetaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customer_module_meta_info(
        self,
        request: main_models.CreateCustomerModuleMetaInfoRequest,
    ) -> main_models.CreateCustomerModuleMetaInfoResponse:
        runtime = RuntimeOptions()
        return self.create_customer_module_meta_info_with_options(request, runtime)

    async def create_customer_module_meta_info_async(
        self,
        request: main_models.CreateCustomerModuleMetaInfoRequest,
    ) -> main_models.CreateCustomerModuleMetaInfoResponse:
        runtime = RuntimeOptions()
        return await self.create_customer_module_meta_info_with_options_async(request, runtime)

    def create_customer_module_output_info_with_options(
        self,
        request: main_models.CreateCustomerModuleOutputInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomerModuleOutputInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        if not DaraCore.is_null(request.final_score_format):
            query['FinalScoreFormat'] = request.final_score_format
        if not DaraCore.is_null(request.process_expression):
            query['ProcessExpression'] = request.process_expression
        if not DaraCore.is_null(request.test_file_url):
            query['TestFileUrl'] = request.test_file_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomerModuleOutputInfo',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomerModuleOutputInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customer_module_output_info_with_options_async(
        self,
        request: main_models.CreateCustomerModuleOutputInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomerModuleOutputInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        if not DaraCore.is_null(request.final_score_format):
            query['FinalScoreFormat'] = request.final_score_format
        if not DaraCore.is_null(request.process_expression):
            query['ProcessExpression'] = request.process_expression
        if not DaraCore.is_null(request.test_file_url):
            query['TestFileUrl'] = request.test_file_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomerModuleOutputInfo',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomerModuleOutputInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customer_module_output_info(
        self,
        request: main_models.CreateCustomerModuleOutputInfoRequest,
    ) -> main_models.CreateCustomerModuleOutputInfoResponse:
        runtime = RuntimeOptions()
        return self.create_customer_module_output_info_with_options(request, runtime)

    async def create_customer_module_output_info_async(
        self,
        request: main_models.CreateCustomerModuleOutputInfoRequest,
    ) -> main_models.CreateCustomerModuleOutputInfoResponse:
        runtime = RuntimeOptions()
        return await self.create_customer_module_output_info_with_options_async(request, runtime)

    def delete_model_with_options(
        self,
        request: main_models.DeleteModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        request: main_models.DeleteModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    async def delete_model_async(
        self,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        return await self.delete_model_with_options_async(request, runtime)

    def describe_customer_module_basic_info_with_options(
        self,
        request: main_models.DescribeCustomerModuleBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomerModuleBasicInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomerModuleBasicInfo',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomerModuleBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customer_module_basic_info_with_options_async(
        self,
        request: main_models.DescribeCustomerModuleBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomerModuleBasicInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomerModuleBasicInfo',
            version = '2025-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomerModuleBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customer_module_basic_info(
        self,
        request: main_models.DescribeCustomerModuleBasicInfoRequest,
    ) -> main_models.DescribeCustomerModuleBasicInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_customer_module_basic_info_with_options(request, runtime)

    async def describe_customer_module_basic_info_async(
        self,
        request: main_models.DescribeCustomerModuleBasicInfoRequest,
    ) -> main_models.DescribeCustomerModuleBasicInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_customer_module_basic_info_with_options_async(request, runtime)
