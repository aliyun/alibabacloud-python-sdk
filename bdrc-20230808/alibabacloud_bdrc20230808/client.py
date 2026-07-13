# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_bdrc20230808 import models as main_models
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
            'cn-shanghai-finance-1': 'bdrc.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shanghai': 'bdrc.cn-shanghai.aliyuncs.com',
            'ap-southeast-1': 'bdrc.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('bdrc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_rules_with_options(
        self,
        request: main_models.CheckRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckRules',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/rules/check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_rules_with_options_async(
        self,
        request: main_models.CheckRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckRules',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/rules/check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_rules(
        self,
        request: main_models.CheckRulesRequest,
    ) -> main_models.CheckRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_rules_with_options(request, headers, runtime)

    async def check_rules_async(
        self,
        request: main_models.CheckRulesRequest,
    ) -> main_models.CheckRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_rules_with_options_async(request, headers, runtime)

    def close_bdrc_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseBdrcServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CloseBdrcService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/service/close',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseBdrcServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_bdrc_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseBdrcServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CloseBdrcService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/service/close',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseBdrcServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_bdrc_service(self) -> main_models.CloseBdrcServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.close_bdrc_service_with_options(headers, runtime)

    async def close_bdrc_service_async(self) -> main_models.CloseBdrcServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.close_bdrc_service_with_options_async(headers, runtime)

    def create_protection_policy_with_options(
        self,
        tmp_req: main_models.CreateProtectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProtectionPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateProtectionPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.bound_resource_category_ids):
            request.bound_resource_category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.bound_resource_category_ids, 'BoundResourceCategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.sub_protection_policies):
            request.sub_protection_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_protection_policies, 'SubProtectionPolicies', 'json')
        body = {}
        if not DaraCore.is_null(request.bound_resource_category_ids_shrink):
            body['BoundResourceCategoryIds'] = request.bound_resource_category_ids_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.protection_policy_name):
            body['ProtectionPolicyName'] = request.protection_policy_name
        if not DaraCore.is_null(request.protection_policy_region_id):
            body['ProtectionPolicyRegionId'] = request.protection_policy_region_id
        if not DaraCore.is_null(request.sub_protection_policies_shrink):
            body['SubProtectionPolicies'] = request.sub_protection_policies_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProtectionPolicy',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProtectionPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_protection_policy_with_options_async(
        self,
        tmp_req: main_models.CreateProtectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProtectionPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateProtectionPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.bound_resource_category_ids):
            request.bound_resource_category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.bound_resource_category_ids, 'BoundResourceCategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.sub_protection_policies):
            request.sub_protection_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_protection_policies, 'SubProtectionPolicies', 'json')
        body = {}
        if not DaraCore.is_null(request.bound_resource_category_ids_shrink):
            body['BoundResourceCategoryIds'] = request.bound_resource_category_ids_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.protection_policy_name):
            body['ProtectionPolicyName'] = request.protection_policy_name
        if not DaraCore.is_null(request.protection_policy_region_id):
            body['ProtectionPolicyRegionId'] = request.protection_policy_region_id
        if not DaraCore.is_null(request.sub_protection_policies_shrink):
            body['SubProtectionPolicies'] = request.sub_protection_policies_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProtectionPolicy',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProtectionPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_protection_policy(
        self,
        request: main_models.CreateProtectionPolicyRequest,
    ) -> main_models.CreateProtectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_protection_policy_with_options(request, headers, runtime)

    async def create_protection_policy_async(
        self,
        request: main_models.CreateProtectionPolicyRequest,
    ) -> main_models.CreateProtectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_protection_policy_with_options_async(request, headers, runtime)

    def create_resource_category_with_options(
        self,
        request: main_models.CreateResourceCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_category_name):
            body['ResourceCategoryName'] = request.resource_category_name
        if not DaraCore.is_null(request.resource_matcher):
            body['ResourceMatcher'] = request.resource_matcher
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceCategory',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_category_with_options_async(
        self,
        request: main_models.CreateResourceCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_category_name):
            body['ResourceCategoryName'] = request.resource_category_name
        if not DaraCore.is_null(request.resource_matcher):
            body['ResourceMatcher'] = request.resource_matcher
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceCategory',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_category(
        self,
        request: main_models.CreateResourceCategoryRequest,
    ) -> main_models.CreateResourceCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_category_with_options(request, headers, runtime)

    async def create_resource_category_async(
        self,
        request: main_models.CreateResourceCategoryRequest,
    ) -> main_models.CreateResourceCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_category_with_options_async(request, headers, runtime)

    def delete_protection_policy_with_options(
        self,
        protection_policy_id: str,
        request: main_models.DeleteProtectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProtectionPolicyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteProtectionPolicy',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies/{DaraURL.percent_encode(protection_policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProtectionPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_protection_policy_with_options_async(
        self,
        protection_policy_id: str,
        request: main_models.DeleteProtectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProtectionPolicyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteProtectionPolicy',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies/{DaraURL.percent_encode(protection_policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProtectionPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_protection_policy(
        self,
        protection_policy_id: str,
        request: main_models.DeleteProtectionPolicyRequest,
    ) -> main_models.DeleteProtectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_protection_policy_with_options(protection_policy_id, request, headers, runtime)

    async def delete_protection_policy_async(
        self,
        protection_policy_id: str,
        request: main_models.DeleteProtectionPolicyRequest,
    ) -> main_models.DeleteProtectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_protection_policy_with_options_async(protection_policy_id, request, headers, runtime)

    def delete_resource_category_with_options(
        self,
        request: main_models.DeleteResourceCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_category_id):
            body['ResourceCategoryId'] = request.resource_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceCategory',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_category_with_options_async(
        self,
        request: main_models.DeleteResourceCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_category_id):
            body['ResourceCategoryId'] = request.resource_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceCategory',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_category(
        self,
        request: main_models.DeleteResourceCategoryRequest,
    ) -> main_models.DeleteResourceCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_category_with_options(request, headers, runtime)

    async def delete_resource_category_async(
        self,
        request: main_models.DeleteResourceCategoryRequest,
    ) -> main_models.DeleteResourceCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_category_with_options_async(request, headers, runtime)

    def describe_check_details_with_options(
        self,
        request: main_models.DescribeCheckDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCheckDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCheckDetails',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/check-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCheckDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_check_details_with_options_async(
        self,
        request: main_models.DescribeCheckDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCheckDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCheckDetails',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/check-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCheckDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_check_details(
        self,
        request: main_models.DescribeCheckDetailsRequest,
    ) -> main_models.DescribeCheckDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_check_details_with_options(request, headers, runtime)

    async def describe_check_details_async(
        self,
        request: main_models.DescribeCheckDetailsRequest,
    ) -> main_models.DescribeCheckDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_check_details_with_options_async(request, headers, runtime)

    def describe_product_data_redundancy_type_stat_with_options(
        self,
        tmp_req: main_models.DescribeProductDataRedundancyTypeStatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductDataRedundancyTypeStatResponse:
        tmp_req.validate()
        request = main_models.DescribeProductDataRedundancyTypeStatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductDataRedundancyTypeStat',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products/data-redundancy-type-stat',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductDataRedundancyTypeStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_data_redundancy_type_stat_with_options_async(
        self,
        tmp_req: main_models.DescribeProductDataRedundancyTypeStatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductDataRedundancyTypeStatResponse:
        tmp_req.validate()
        request = main_models.DescribeProductDataRedundancyTypeStatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductDataRedundancyTypeStat',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products/data-redundancy-type-stat',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductDataRedundancyTypeStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_data_redundancy_type_stat(
        self,
        request: main_models.DescribeProductDataRedundancyTypeStatRequest,
    ) -> main_models.DescribeProductDataRedundancyTypeStatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_product_data_redundancy_type_stat_with_options(request, headers, runtime)

    async def describe_product_data_redundancy_type_stat_async(
        self,
        request: main_models.DescribeProductDataRedundancyTypeStatRequest,
    ) -> main_models.DescribeProductDataRedundancyTypeStatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_product_data_redundancy_type_stat_with_options_async(request, headers, runtime)

    def describe_products_with_options(
        self,
        tmp_req: main_models.DescribeProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductsResponse:
        tmp_req.validate()
        request = main_models.DescribeProductsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProducts',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_products_with_options_async(
        self,
        tmp_req: main_models.DescribeProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductsResponse:
        tmp_req.validate()
        request = main_models.DescribeProductsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProducts',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_products(
        self,
        request: main_models.DescribeProductsRequest,
    ) -> main_models.DescribeProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_products_with_options(request, headers, runtime)

    async def describe_products_async(
        self,
        request: main_models.DescribeProductsRequest,
    ) -> main_models.DescribeProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_products_with_options_async(request, headers, runtime)

    def describe_resources_with_options(
        self,
        tmp_req: main_models.DescribeResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourcesResponse:
        tmp_req.validate()
        request = main_models.DescribeResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.data_redundancy_type):
            query['DataRedundancyType'] = request.data_redundancy_type
        if not DaraCore.is_null(request.failed_rule_template):
            query['FailedRuleTemplate'] = request.failed_rule_template
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResources',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resources_with_options_async(
        self,
        tmp_req: main_models.DescribeResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourcesResponse:
        tmp_req.validate()
        request = main_models.DescribeResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.data_redundancy_type):
            query['DataRedundancyType'] = request.data_redundancy_type
        if not DaraCore.is_null(request.failed_rule_template):
            query['FailedRuleTemplate'] = request.failed_rule_template
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResources',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resources(
        self,
        request: main_models.DescribeResourcesRequest,
    ) -> main_models.DescribeResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_resources_with_options(request, headers, runtime)

    async def describe_resources_async(
        self,
        request: main_models.DescribeResourcesRequest,
    ) -> main_models.DescribeResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_resources_with_options_async(request, headers, runtime)

    def describe_rules_with_options(
        self,
        tmp_req: main_models.DescribeRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRulesResponse:
        tmp_req.validate()
        request = main_models.DescribeRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRules',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        tmp_req: main_models.DescribeRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRulesResponse:
        tmp_req.validate()
        request = main_models.DescribeRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRules',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.describe_rules_with_options(request, headers, runtime)

    async def describe_rules_async(
        self,
        request: main_models.DescribeRulesRequest,
    ) -> main_models.DescribeRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_rules_with_options_async(request, headers, runtime)

    def describe_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeTask',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeTask',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task(
        self,
        task_id: str,
    ) -> main_models.DescribeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_task_with_options(task_id, headers, runtime)

    async def describe_task_async(
        self,
        task_id: str,
    ) -> main_models.DescribeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_task_with_options_async(task_id, headers, runtime)

    def describe_tasks_with_options(
        self,
        request: main_models.DescribeTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTasks',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: main_models.DescribeTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTasks',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: main_models.DescribeTasksRequest,
    ) -> main_models.DescribeTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_tasks_with_options(request, headers, runtime)

    async def describe_tasks_async(
        self,
        request: main_models.DescribeTasksRequest,
    ) -> main_models.DescribeTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_tasks_with_options_async(request, headers, runtime)

    def describe_top_risky_resources_with_options(
        self,
        tmp_req: main_models.DescribeTopRiskyResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTopRiskyResourcesResponse:
        tmp_req.validate()
        request = main_models.DescribeTopRiskyResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTopRiskyResources',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/top-risky',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTopRiskyResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_risky_resources_with_options_async(
        self,
        tmp_req: main_models.DescribeTopRiskyResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTopRiskyResourcesResponse:
        tmp_req.validate()
        request = main_models.DescribeTopRiskyResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_owner_ids):
            request.resource_owner_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_owner_ids, 'ResourceOwnerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_owner_ids_shrink):
            query['ResourceOwnerIds'] = request.resource_owner_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTopRiskyResources',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/top-risky',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTopRiskyResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_top_risky_resources(
        self,
        request: main_models.DescribeTopRiskyResourcesRequest,
    ) -> main_models.DescribeTopRiskyResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_top_risky_resources_with_options(request, headers, runtime)

    async def describe_top_risky_resources_async(
        self,
        request: main_models.DescribeTopRiskyResourcesRequest,
    ) -> main_models.DescribeTopRiskyResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_top_risky_resources_with_options_async(request, headers, runtime)

    def disable_check_product_with_options(
        self,
        request: main_models.DisableCheckProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableCheckProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableCheckProduct',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products/disable-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCheckProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_check_product_with_options_async(
        self,
        request: main_models.DisableCheckProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableCheckProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableCheckProduct',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products/disable-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCheckProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_check_product(
        self,
        request: main_models.DisableCheckProductRequest,
    ) -> main_models.DisableCheckProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_check_product_with_options(request, headers, runtime)

    async def disable_check_product_async(
        self,
        request: main_models.DisableCheckProductRequest,
    ) -> main_models.DisableCheckProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_check_product_with_options_async(request, headers, runtime)

    def disable_check_resource_with_options(
        self,
        request: main_models.DisableCheckResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableCheckResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableCheckResource',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/disable-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCheckResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_check_resource_with_options_async(
        self,
        request: main_models.DisableCheckResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableCheckResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableCheckResource',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/disable-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCheckResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_check_resource(
        self,
        request: main_models.DisableCheckResourceRequest,
    ) -> main_models.DisableCheckResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_check_resource_with_options(request, headers, runtime)

    async def disable_check_resource_async(
        self,
        request: main_models.DisableCheckResourceRequest,
    ) -> main_models.DisableCheckResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_check_resource_with_options_async(request, headers, runtime)

    def enable_check_product_with_options(
        self,
        request: main_models.EnableCheckProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableCheckProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableCheckProduct',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products/enable-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCheckProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_check_product_with_options_async(
        self,
        request: main_models.EnableCheckProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableCheckProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableCheckProduct',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/products/enable-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCheckProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_check_product(
        self,
        request: main_models.EnableCheckProductRequest,
    ) -> main_models.EnableCheckProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_check_product_with_options(request, headers, runtime)

    async def enable_check_product_async(
        self,
        request: main_models.EnableCheckProductRequest,
    ) -> main_models.EnableCheckProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_check_product_with_options_async(request, headers, runtime)

    def enable_check_resource_with_options(
        self,
        request: main_models.EnableCheckResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableCheckResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableCheckResource',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/enable-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCheckResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_check_resource_with_options_async(
        self,
        request: main_models.EnableCheckResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableCheckResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableCheckResource',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/enable-check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCheckResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_check_resource(
        self,
        request: main_models.EnableCheckResourceRequest,
    ) -> main_models.EnableCheckResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_check_resource_with_options(request, headers, runtime)

    async def enable_check_resource_async(
        self,
        request: main_models.EnableCheckResourceRequest,
    ) -> main_models.EnableCheckResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_check_resource_with_options_async(request, headers, runtime)

    def get_bdrc_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBdrcServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBdrcService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/service',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBdrcServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bdrc_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBdrcServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBdrcService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/service',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBdrcServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bdrc_service(self) -> main_models.GetBdrcServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_bdrc_service_with_options(headers, runtime)

    async def get_bdrc_service_async(self) -> main_models.GetBdrcServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_bdrc_service_with_options_async(headers, runtime)

    def get_message_with_options(
        self,
        message_id: str,
        request: main_models.GetMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMessage',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/messages/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_with_options_async(
        self,
        message_id: str,
        request: main_models.GetMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMessage',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/messages/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message(
        self,
        message_id: str,
        request: main_models.GetMessageRequest,
    ) -> main_models.GetMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_message_with_options(message_id, request, headers, runtime)

    async def get_message_async(
        self,
        message_id: str,
        request: main_models.GetMessageRequest,
    ) -> main_models.GetMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_message_with_options_async(message_id, request, headers, runtime)

    def get_protection_policy_with_options(
        self,
        protection_policy_id: str,
        request: main_models.GetProtectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProtectionPolicyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProtectionPolicy',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies/{DaraURL.percent_encode(protection_policy_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProtectionPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_protection_policy_with_options_async(
        self,
        protection_policy_id: str,
        request: main_models.GetProtectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProtectionPolicyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProtectionPolicy',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies/{DaraURL.percent_encode(protection_policy_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProtectionPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_protection_policy(
        self,
        protection_policy_id: str,
        request: main_models.GetProtectionPolicyRequest,
    ) -> main_models.GetProtectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_protection_policy_with_options(protection_policy_id, request, headers, runtime)

    async def get_protection_policy_async(
        self,
        protection_policy_id: str,
        request: main_models.GetProtectionPolicyRequest,
    ) -> main_models.GetProtectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_protection_policy_with_options_async(protection_policy_id, request, headers, runtime)

    def get_resource_category_with_options(
        self,
        request: main_models.GetResourceCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceCategory',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_category_with_options_async(
        self,
        request: main_models.GetResourceCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceCategory',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_category(
        self,
        request: main_models.GetResourceCategoryRequest,
    ) -> main_models.GetResourceCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_category_with_options(request, headers, runtime)

    async def get_resource_category_async(
        self,
        request: main_models.GetResourceCategoryRequest,
    ) -> main_models.GetResourceCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_category_with_options_async(request, headers, runtime)

    def list_messages_with_options(
        self,
        request: main_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.message_level):
            query['MessageLevel'] = request.message_level
        if not DaraCore.is_null(request.message_time_earlier_than):
            query['MessageTimeEarlierThan'] = request.message_time_earlier_than
        if not DaraCore.is_null(request.message_time_later_than):
            query['MessageTimeLaterThan'] = request.message_time_later_than
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessages',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_messages_with_options_async(
        self,
        request: main_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.message_level):
            query['MessageLevel'] = request.message_level
        if not DaraCore.is_null(request.message_time_earlier_than):
            query['MessageTimeEarlierThan'] = request.message_time_earlier_than
        if not DaraCore.is_null(request.message_time_later_than):
            query['MessageTimeLaterThan'] = request.message_time_later_than
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessages',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_messages(
        self,
        request: main_models.ListMessagesRequest,
    ) -> main_models.ListMessagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_messages_with_options(request, headers, runtime)

    async def list_messages_async(
        self,
        request: main_models.ListMessagesRequest,
    ) -> main_models.ListMessagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_messages_with_options_async(request, headers, runtime)

    def list_protection_policies_with_options(
        self,
        request: main_models.ListProtectionPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProtectionPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.protection_policy_id):
            query['ProtectionPolicyId'] = request.protection_policy_id
        if not DaraCore.is_null(request.protection_policy_region_id):
            query['ProtectionPolicyRegionId'] = request.protection_policy_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProtectionPolicies',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProtectionPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_protection_policies_with_options_async(
        self,
        request: main_models.ListProtectionPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProtectionPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.protection_policy_id):
            query['ProtectionPolicyId'] = request.protection_policy_id
        if not DaraCore.is_null(request.protection_policy_region_id):
            query['ProtectionPolicyRegionId'] = request.protection_policy_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProtectionPolicies',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProtectionPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_protection_policies(
        self,
        request: main_models.ListProtectionPoliciesRequest,
    ) -> main_models.ListProtectionPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_protection_policies_with_options(request, headers, runtime)

    async def list_protection_policies_async(
        self,
        request: main_models.ListProtectionPoliciesRequest,
    ) -> main_models.ListProtectionPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_protection_policies_with_options_async(request, headers, runtime)

    def list_protection_policy_applications_with_options(
        self,
        protection_policy_id: str,
        request: main_models.ListProtectionPolicyApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProtectionPolicyApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apply_status):
            query['ApplyStatus'] = request.apply_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sub_protection_policy_type):
            query['SubProtectionPolicyType'] = request.sub_protection_policy_type
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProtectionPolicyApplications',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies/{DaraURL.percent_encode(protection_policy_id)}/list-applications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProtectionPolicyApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_protection_policy_applications_with_options_async(
        self,
        protection_policy_id: str,
        request: main_models.ListProtectionPolicyApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProtectionPolicyApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apply_status):
            query['ApplyStatus'] = request.apply_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sub_protection_policy_type):
            query['SubProtectionPolicyType'] = request.sub_protection_policy_type
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProtectionPolicyApplications',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies/{DaraURL.percent_encode(protection_policy_id)}/list-applications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProtectionPolicyApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_protection_policy_applications(
        self,
        protection_policy_id: str,
        request: main_models.ListProtectionPolicyApplicationsRequest,
    ) -> main_models.ListProtectionPolicyApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_protection_policy_applications_with_options(protection_policy_id, request, headers, runtime)

    async def list_protection_policy_applications_async(
        self,
        protection_policy_id: str,
        request: main_models.ListProtectionPolicyApplicationsRequest,
    ) -> main_models.ListProtectionPolicyApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_protection_policy_applications_with_options_async(protection_policy_id, request, headers, runtime)

    def list_resource_categories_with_options(
        self,
        request: main_models.ListResourceCategoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceCategories',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_categories_with_options_async(
        self,
        request: main_models.ListResourceCategoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_category_id):
            query['ResourceCategoryId'] = request.resource_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceCategories',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_categories(
        self,
        request: main_models.ListResourceCategoriesRequest,
    ) -> main_models.ListResourceCategoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_categories_with_options(request, headers, runtime)

    async def list_resource_categories_async(
        self,
        request: main_models.ListResourceCategoriesRequest,
    ) -> main_models.ListResourceCategoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_categories_with_options_async(request, headers, runtime)

    def open_bdrc_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenBdrcServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'OpenBdrcService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/service/open',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenBdrcServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_bdrc_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenBdrcServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'OpenBdrcService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/service/open',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenBdrcServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_bdrc_service(self) -> main_models.OpenBdrcServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_bdrc_service_with_options(headers, runtime)

    async def open_bdrc_service_async(self) -> main_models.OpenBdrcServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_bdrc_service_with_options_async(headers, runtime)

    def update_protection_policy_with_options(
        self,
        protection_policy_id: str,
        tmp_req: main_models.UpdateProtectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProtectionPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateProtectionPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.bound_resource_category_ids):
            request.bound_resource_category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.bound_resource_category_ids, 'BoundResourceCategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.sub_protection_policies):
            request.sub_protection_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_protection_policies, 'SubProtectionPolicies', 'json')
        body = {}
        if not DaraCore.is_null(request.bound_resource_category_ids_shrink):
            body['BoundResourceCategoryIds'] = request.bound_resource_category_ids_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.protection_policy_name):
            body['ProtectionPolicyName'] = request.protection_policy_name
        if not DaraCore.is_null(request.sub_protection_policies_shrink):
            body['SubProtectionPolicies'] = request.sub_protection_policies_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProtectionPolicy',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies/{DaraURL.percent_encode(protection_policy_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProtectionPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_protection_policy_with_options_async(
        self,
        protection_policy_id: str,
        tmp_req: main_models.UpdateProtectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProtectionPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateProtectionPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.bound_resource_category_ids):
            request.bound_resource_category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.bound_resource_category_ids, 'BoundResourceCategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.sub_protection_policies):
            request.sub_protection_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_protection_policies, 'SubProtectionPolicies', 'json')
        body = {}
        if not DaraCore.is_null(request.bound_resource_category_ids_shrink):
            body['BoundResourceCategoryIds'] = request.bound_resource_category_ids_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.protection_policy_name):
            body['ProtectionPolicyName'] = request.protection_policy_name
        if not DaraCore.is_null(request.sub_protection_policies_shrink):
            body['SubProtectionPolicies'] = request.sub_protection_policies_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProtectionPolicy',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/protection-policies/{DaraURL.percent_encode(protection_policy_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProtectionPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_protection_policy(
        self,
        protection_policy_id: str,
        request: main_models.UpdateProtectionPolicyRequest,
    ) -> main_models.UpdateProtectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_protection_policy_with_options(protection_policy_id, request, headers, runtime)

    async def update_protection_policy_async(
        self,
        protection_policy_id: str,
        request: main_models.UpdateProtectionPolicyRequest,
    ) -> main_models.UpdateProtectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_protection_policy_with_options_async(protection_policy_id, request, headers, runtime)

    def update_resource_category_with_options(
        self,
        request: main_models.UpdateResourceCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_category_id):
            body['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_category_name):
            body['ResourceCategoryName'] = request.resource_category_name
        if not DaraCore.is_null(request.resource_matcher):
            body['ResourceMatcher'] = request.resource_matcher
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceCategory',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_category_with_options_async(
        self,
        request: main_models.UpdateResourceCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_category_id):
            body['ResourceCategoryId'] = request.resource_category_id
        if not DaraCore.is_null(request.resource_category_name):
            body['ResourceCategoryName'] = request.resource_category_name
        if not DaraCore.is_null(request.resource_matcher):
            body['ResourceMatcher'] = request.resource_matcher
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceCategory',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resource-categories/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_category(
        self,
        request: main_models.UpdateResourceCategoryRequest,
    ) -> main_models.UpdateResourceCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_category_with_options(request, headers, runtime)

    async def update_resource_category_async(
        self,
        request: main_models.UpdateResourceCategoryRequest,
    ) -> main_models.UpdateResourceCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_category_with_options_async(request, headers, runtime)

    def update_resources_with_options(
        self,
        request: main_models.UpdateResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResources',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resources_with_options_async(
        self,
        request: main_models.UpdateResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResources',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resources(
        self,
        request: main_models.UpdateResourcesRequest,
    ) -> main_models.UpdateResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resources_with_options(request, headers, runtime)

    async def update_resources_async(
        self,
        request: main_models.UpdateResourcesRequest,
    ) -> main_models.UpdateResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resources_with_options_async(request, headers, runtime)
