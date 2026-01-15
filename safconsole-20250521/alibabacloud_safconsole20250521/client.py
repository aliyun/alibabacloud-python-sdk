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

    def describe_customer_module_meta_info_with_options(
        self,
        request: main_models.DescribeCustomerModuleMetaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomerModuleMetaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomerModuleMetaInfo',
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
            main_models.DescribeCustomerModuleMetaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customer_module_meta_info_with_options_async(
        self,
        request: main_models.DescribeCustomerModuleMetaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomerModuleMetaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomerModuleMetaInfo',
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
            main_models.DescribeCustomerModuleMetaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customer_module_meta_info(
        self,
        request: main_models.DescribeCustomerModuleMetaInfoRequest,
    ) -> main_models.DescribeCustomerModuleMetaInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_customer_module_meta_info_with_options(request, runtime)

    async def describe_customer_module_meta_info_async(
        self,
        request: main_models.DescribeCustomerModuleMetaInfoRequest,
    ) -> main_models.DescribeCustomerModuleMetaInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_customer_module_meta_info_with_options_async(request, runtime)

    def describe_customer_module_output_info_with_options(
        self,
        request: main_models.DescribeCustomerModuleOutputInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomerModuleOutputInfoResponse:
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
            action = 'DescribeCustomerModuleOutputInfo',
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
            main_models.DescribeCustomerModuleOutputInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customer_module_output_info_with_options_async(
        self,
        request: main_models.DescribeCustomerModuleOutputInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomerModuleOutputInfoResponse:
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
            action = 'DescribeCustomerModuleOutputInfo',
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
            main_models.DescribeCustomerModuleOutputInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customer_module_output_info(
        self,
        request: main_models.DescribeCustomerModuleOutputInfoRequest,
    ) -> main_models.DescribeCustomerModuleOutputInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_customer_module_output_info_with_options(request, runtime)

    async def describe_customer_module_output_info_async(
        self,
        request: main_models.DescribeCustomerModuleOutputInfoRequest,
    ) -> main_models.DescribeCustomerModuleOutputInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_customer_module_output_info_with_options_async(request, runtime)

    def describe_feature_option_with_options(
        self,
        request: main_models.DescribeFeatureOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFeatureOptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_template):
            query['FeatureTemplate'] = request.feature_template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFeatureOption',
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
            main_models.DescribeFeatureOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_feature_option_with_options_async(
        self,
        request: main_models.DescribeFeatureOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFeatureOptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_template):
            query['FeatureTemplate'] = request.feature_template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFeatureOption',
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
            main_models.DescribeFeatureOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_feature_option(
        self,
        request: main_models.DescribeFeatureOptionRequest,
    ) -> main_models.DescribeFeatureOptionResponse:
        runtime = RuntimeOptions()
        return self.describe_feature_option_with_options(request, runtime)

    async def describe_feature_option_async(
        self,
        request: main_models.DescribeFeatureOptionRequest,
    ) -> main_models.DescribeFeatureOptionResponse:
        runtime = RuntimeOptions()
        return await self.describe_feature_option_with_options_async(request, runtime)

    def describe_feature_template_list_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFeatureTemplateListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeFeatureTemplateList',
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
            main_models.DescribeFeatureTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_feature_template_list_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFeatureTemplateListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeFeatureTemplateList',
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
            main_models.DescribeFeatureTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_feature_template_list(self) -> main_models.DescribeFeatureTemplateListResponse:
        runtime = RuntimeOptions()
        return self.describe_feature_template_list_with_options(runtime)

    async def describe_feature_template_list_async(self) -> main_models.DescribeFeatureTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_feature_template_list_with_options_async(runtime)

    def describe_model_feature_with_options(
        self,
        request: main_models.DescribeModelFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        if not DaraCore.is_null(request.feature_template):
            query['FeatureTemplate'] = request.feature_template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelFeature',
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
            main_models.DescribeModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_model_feature_with_options_async(
        self,
        request: main_models.DescribeModelFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        if not DaraCore.is_null(request.feature_template):
            query['FeatureTemplate'] = request.feature_template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModelFeature',
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
            main_models.DescribeModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_model_feature(
        self,
        request: main_models.DescribeModelFeatureRequest,
    ) -> main_models.DescribeModelFeatureResponse:
        runtime = RuntimeOptions()
        return self.describe_model_feature_with_options(request, runtime)

    async def describe_model_feature_async(
        self,
        request: main_models.DescribeModelFeatureRequest,
    ) -> main_models.DescribeModelFeatureResponse:
        runtime = RuntimeOptions()
        return await self.describe_model_feature_with_options_async(request, runtime)

    def describe_model_oss_token_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelOssTokenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeModelOssToken',
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
            main_models.DescribeModelOssTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_model_oss_token_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelOssTokenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeModelOssToken',
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
            main_models.DescribeModelOssTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_model_oss_token(self) -> main_models.DescribeModelOssTokenResponse:
        runtime = RuntimeOptions()
        return self.describe_model_oss_token_with_options(runtime)

    async def describe_model_oss_token_async(self) -> main_models.DescribeModelOssTokenResponse:
        runtime = RuntimeOptions()
        return await self.describe_model_oss_token_with_options_async(runtime)

    def describe_module_service_exist_with_options(
        self,
        request: main_models.DescribeModuleServiceExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModuleServiceExistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModuleServiceExist',
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
            main_models.DescribeModuleServiceExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_module_service_exist_with_options_async(
        self,
        request: main_models.DescribeModuleServiceExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModuleServiceExistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModuleServiceExist',
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
            main_models.DescribeModuleServiceExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_module_service_exist(
        self,
        request: main_models.DescribeModuleServiceExistRequest,
    ) -> main_models.DescribeModuleServiceExistResponse:
        runtime = RuntimeOptions()
        return self.describe_module_service_exist_with_options(request, runtime)

    async def describe_module_service_exist_async(
        self,
        request: main_models.DescribeModuleServiceExistRequest,
    ) -> main_models.DescribeModuleServiceExistResponse:
        runtime = RuntimeOptions()
        return await self.describe_module_service_exist_with_options_async(request, runtime)

    def describe_module_status_with_options(
        self,
        request: main_models.DescribeModuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModuleStatus',
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
            main_models.DescribeModuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_module_status_with_options_async(
        self,
        request: main_models.DescribeModuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModuleStatus',
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
            main_models.DescribeModuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_module_status(
        self,
        request: main_models.DescribeModuleStatusRequest,
    ) -> main_models.DescribeModuleStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_module_status_with_options(request, runtime)

    async def describe_module_status_async(
        self,
        request: main_models.DescribeModuleStatusRequest,
    ) -> main_models.DescribeModuleStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_module_status_with_options_async(request, runtime)

    def describe_saf_rmmp_order_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafRmmpOrderResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSafRmmpOrder',
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
            main_models.DescribeSafRmmpOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_saf_rmmp_order_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSafRmmpOrderResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSafRmmpOrder',
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
            main_models.DescribeSafRmmpOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_saf_rmmp_order(self) -> main_models.DescribeSafRmmpOrderResponse:
        runtime = RuntimeOptions()
        return self.describe_saf_rmmp_order_with_options(runtime)

    async def describe_saf_rmmp_order_async(self) -> main_models.DescribeSafRmmpOrderResponse:
        runtime = RuntimeOptions()
        return await self.describe_saf_rmmp_order_with_options_async(runtime)

    def describe_service_and_scene_with_options(
        self,
        request: main_models.DescribeServiceAndSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceAndSceneResponse:
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
            action = 'DescribeServiceAndScene',
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
            main_models.DescribeServiceAndSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_and_scene_with_options_async(
        self,
        request: main_models.DescribeServiceAndSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceAndSceneResponse:
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
            action = 'DescribeServiceAndScene',
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
            main_models.DescribeServiceAndSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_and_scene(
        self,
        request: main_models.DescribeServiceAndSceneRequest,
    ) -> main_models.DescribeServiceAndSceneResponse:
        runtime = RuntimeOptions()
        return self.describe_service_and_scene_with_options(request, runtime)

    async def describe_service_and_scene_async(
        self,
        request: main_models.DescribeServiceAndSceneRequest,
    ) -> main_models.DescribeServiceAndSceneResponse:
        runtime = RuntimeOptions()
        return await self.describe_service_and_scene_with_options_async(request, runtime)

    def describe_user_model_list_with_options(
        self,
        request: main_models.DescribeUserModelListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserModelListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserModelList',
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
            main_models.DescribeUserModelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_model_list_with_options_async(
        self,
        request: main_models.DescribeUserModelListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserModelListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserModelList',
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
            main_models.DescribeUserModelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_model_list(
        self,
        request: main_models.DescribeUserModelListRequest,
    ) -> main_models.DescribeUserModelListResponse:
        runtime = RuntimeOptions()
        return self.describe_user_model_list_with_options(request, runtime)

    async def describe_user_model_list_async(
        self,
        request: main_models.DescribeUserModelListRequest,
    ) -> main_models.DescribeUserModelListResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_model_list_with_options_async(request, runtime)

    def duplicate_model_with_options(
        self,
        request: main_models.DuplicateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DuplicateModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DuplicateModel',
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
            main_models.DuplicateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def duplicate_model_with_options_async(
        self,
        request: main_models.DuplicateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DuplicateModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DuplicateModel',
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
            main_models.DuplicateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def duplicate_model(
        self,
        request: main_models.DuplicateModelRequest,
    ) -> main_models.DuplicateModelResponse:
        runtime = RuntimeOptions()
        return self.duplicate_model_with_options(request, runtime)

    async def duplicate_model_async(
        self,
        request: main_models.DuplicateModelRequest,
    ) -> main_models.DuplicateModelResponse:
        runtime = RuntimeOptions()
        return await self.duplicate_model_with_options_async(request, runtime)

    def edit_model_with_options(
        self,
        request: main_models.EditModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditModel',
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
            main_models.EditModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_model_with_options_async(
        self,
        request: main_models.EditModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditModel',
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
            main_models.EditModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_model(
        self,
        request: main_models.EditModelRequest,
    ) -> main_models.EditModelResponse:
        runtime = RuntimeOptions()
        return self.edit_model_with_options(request, runtime)

    async def edit_model_async(
        self,
        request: main_models.EditModelRequest,
    ) -> main_models.EditModelResponse:
        runtime = RuntimeOptions()
        return await self.edit_model_with_options_async(request, runtime)

    def iterate_model_with_options(
        self,
        request: main_models.IterateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IterateModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IterateModel',
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
            main_models.IterateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def iterate_model_with_options_async(
        self,
        request: main_models.IterateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IterateModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IterateModel',
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
            main_models.IterateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def iterate_model(
        self,
        request: main_models.IterateModelRequest,
    ) -> main_models.IterateModelResponse:
        runtime = RuntimeOptions()
        return self.iterate_model_with_options(request, runtime)

    async def iterate_model_async(
        self,
        request: main_models.IterateModelRequest,
    ) -> main_models.IterateModelResponse:
        runtime = RuntimeOptions()
        return await self.iterate_model_with_options_async(request, runtime)

    def offline_model_with_options(
        self,
        request: main_models.OfflineModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineModel',
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
            main_models.OfflineModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_model_with_options_async(
        self,
        request: main_models.OfflineModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineModel',
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
            main_models.OfflineModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_model(
        self,
        request: main_models.OfflineModelRequest,
    ) -> main_models.OfflineModelResponse:
        runtime = RuntimeOptions()
        return self.offline_model_with_options(request, runtime)

    async def offline_model_async(
        self,
        request: main_models.OfflineModelRequest,
    ) -> main_models.OfflineModelResponse:
        runtime = RuntimeOptions()
        return await self.offline_model_with_options_async(request, runtime)

    def online_model_with_options(
        self,
        request: main_models.OnlineModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnlineModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnlineModel',
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
            main_models.OnlineModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_model_with_options_async(
        self,
        request: main_models.OnlineModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnlineModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnlineModel',
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
            main_models.OnlineModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_model(
        self,
        request: main_models.OnlineModelRequest,
    ) -> main_models.OnlineModelResponse:
        runtime = RuntimeOptions()
        return self.online_model_with_options(request, runtime)

    async def online_model_async(
        self,
        request: main_models.OnlineModelRequest,
    ) -> main_models.OnlineModelResponse:
        runtime = RuntimeOptions()
        return await self.online_model_with_options_async(request, runtime)

    def parse_expression_parameters_with_options(
        self,
        request: main_models.ParseExpressionParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ParseExpressionParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ParseExpressionParameters',
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
            main_models.ParseExpressionParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def parse_expression_parameters_with_options_async(
        self,
        request: main_models.ParseExpressionParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ParseExpressionParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ParseExpressionParameters',
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
            main_models.ParseExpressionParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def parse_expression_parameters(
        self,
        request: main_models.ParseExpressionParametersRequest,
    ) -> main_models.ParseExpressionParametersResponse:
        runtime = RuntimeOptions()
        return self.parse_expression_parameters_with_options(request, runtime)

    async def parse_expression_parameters_async(
        self,
        request: main_models.ParseExpressionParametersRequest,
    ) -> main_models.ParseExpressionParametersResponse:
        runtime = RuntimeOptions()
        return await self.parse_expression_parameters_with_options_async(request, runtime)

    def prepublish_model_with_options(
        self,
        request: main_models.PrepublishModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PrepublishModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PrepublishModel',
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
            main_models.PrepublishModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def prepublish_model_with_options_async(
        self,
        request: main_models.PrepublishModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PrepublishModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PrepublishModel',
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
            main_models.PrepublishModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def prepublish_model(
        self,
        request: main_models.PrepublishModelRequest,
    ) -> main_models.PrepublishModelResponse:
        runtime = RuntimeOptions()
        return self.prepublish_model_with_options(request, runtime)

    async def prepublish_model_async(
        self,
        request: main_models.PrepublishModelRequest,
    ) -> main_models.PrepublishModelResponse:
        runtime = RuntimeOptions()
        return await self.prepublish_model_with_options_async(request, runtime)

    def rollback_model_with_options(
        self,
        request: main_models.RollbackModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackModel',
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
            main_models.RollbackModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_model_with_options_async(
        self,
        request: main_models.RollbackModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackModel',
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
            main_models.RollbackModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_model(
        self,
        request: main_models.RollbackModelRequest,
    ) -> main_models.RollbackModelResponse:
        runtime = RuntimeOptions()
        return self.rollback_model_with_options(request, runtime)

    async def rollback_model_async(
        self,
        request: main_models.RollbackModelRequest,
    ) -> main_models.RollbackModelResponse:
        runtime = RuntimeOptions()
        return await self.rollback_model_with_options_async(request, runtime)

    def test_model_with_options(
        self,
        request: main_models.TestModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TestModel',
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
            main_models.TestModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_model_with_options_async(
        self,
        request: main_models.TestModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TestModel',
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
            main_models.TestModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_model(
        self,
        request: main_models.TestModelRequest,
    ) -> main_models.TestModelResponse:
        runtime = RuntimeOptions()
        return self.test_model_with_options(request, runtime)

    async def test_model_async(
        self,
        request: main_models.TestModelRequest,
    ) -> main_models.TestModelResponse:
        runtime = RuntimeOptions()
        return await self.test_model_with_options_async(request, runtime)

    def test_pre_model_with_options(
        self,
        request: main_models.TestPreModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestPreModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TestPreModel',
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
            main_models.TestPreModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_pre_model_with_options_async(
        self,
        request: main_models.TestPreModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestPreModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TestPreModel',
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
            main_models.TestPreModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_pre_model(
        self,
        request: main_models.TestPreModelRequest,
    ) -> main_models.TestPreModelResponse:
        runtime = RuntimeOptions()
        return self.test_pre_model_with_options(request, runtime)

    async def test_pre_model_async(
        self,
        request: main_models.TestPreModelRequest,
    ) -> main_models.TestPreModelResponse:
        runtime = RuntimeOptions()
        return await self.test_pre_model_with_options_async(request, runtime)

    def test_process_expression_with_options(
        self,
        request: main_models.TestProcessExpressionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestProcessExpressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TestProcessExpression',
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
            main_models.TestProcessExpressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_process_expression_with_options_async(
        self,
        request: main_models.TestProcessExpressionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestProcessExpressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TestProcessExpression',
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
            main_models.TestProcessExpressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_process_expression(
        self,
        request: main_models.TestProcessExpressionRequest,
    ) -> main_models.TestProcessExpressionResponse:
        runtime = RuntimeOptions()
        return self.test_process_expression_with_options(request, runtime)

    async def test_process_expression_async(
        self,
        request: main_models.TestProcessExpressionRequest,
    ) -> main_models.TestProcessExpressionResponse:
        runtime = RuntimeOptions()
        return await self.test_process_expression_with_options_async(request, runtime)

    def update_module_basic_info_with_options(
        self,
        request: main_models.UpdateModuleBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModuleBasicInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
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
            action = 'UpdateModuleBasicInfo',
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
            main_models.UpdateModuleBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_module_basic_info_with_options_async(
        self,
        request: main_models.UpdateModuleBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModuleBasicInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
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
            action = 'UpdateModuleBasicInfo',
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
            main_models.UpdateModuleBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_module_basic_info(
        self,
        request: main_models.UpdateModuleBasicInfoRequest,
    ) -> main_models.UpdateModuleBasicInfoResponse:
        runtime = RuntimeOptions()
        return self.update_module_basic_info_with_options(request, runtime)

    async def update_module_basic_info_async(
        self,
        request: main_models.UpdateModuleBasicInfoRequest,
    ) -> main_models.UpdateModuleBasicInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_module_basic_info_with_options_async(request, runtime)

    def validate_model_file_with_options(
        self,
        request: main_models.ValidateModelFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateModelFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateModelFile',
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
            main_models.ValidateModelFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_model_file_with_options_async(
        self,
        request: main_models.ValidateModelFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateModelFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateModelFile',
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
            main_models.ValidateModelFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_model_file(
        self,
        request: main_models.ValidateModelFileRequest,
    ) -> main_models.ValidateModelFileResponse:
        runtime = RuntimeOptions()
        return self.validate_model_file_with_options(request, runtime)

    async def validate_model_file_async(
        self,
        request: main_models.ValidateModelFileRequest,
    ) -> main_models.ValidateModelFileResponse:
        runtime = RuntimeOptions()
        return await self.validate_model_file_with_options_async(request, runtime)

    def validate_test_file_with_options(
        self,
        request: main_models.ValidateTestFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateTestFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateTestFile',
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
            main_models.ValidateTestFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_test_file_with_options_async(
        self,
        request: main_models.ValidateTestFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateTestFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_module_id):
            query['CustomerModuleId'] = request.customer_module_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateTestFile',
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
            main_models.ValidateTestFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_test_file(
        self,
        request: main_models.ValidateTestFileRequest,
    ) -> main_models.ValidateTestFileResponse:
        runtime = RuntimeOptions()
        return self.validate_test_file_with_options(request, runtime)

    async def validate_test_file_async(
        self,
        request: main_models.ValidateTestFileRequest,
    ) -> main_models.ValidateTestFileResponse:
        runtime = RuntimeOptions()
        return await self.validate_test_file_with_options_async(request, runtime)
