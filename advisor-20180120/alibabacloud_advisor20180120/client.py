# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_advisor20180120 import models as main_models
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
        self._endpoint = self.get_endpoint('advisor', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_advices_with_options(
        self,
        request: main_models.DescribeAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.exclude_advice_id):
            query['ExcludeAdviceId'] = request.exclude_advice_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advices_with_options_async(
        self,
        request: main_models.DescribeAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.exclude_advice_id):
            query['ExcludeAdviceId'] = request.exclude_advice_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advices(
        self,
        request: main_models.DescribeAdvicesRequest,
    ) -> main_models.DescribeAdvicesResponse:
        runtime = RuntimeOptions()
        return self.describe_advices_with_options(request, runtime)

    async def describe_advices_async(
        self,
        request: main_models.DescribeAdvicesRequest,
    ) -> main_models.DescribeAdvicesResponse:
        runtime = RuntimeOptions()
        return await self.describe_advices_with_options_async(request, runtime)

    def describe_advices_flat_page_with_options(
        self,
        request: main_models.DescribeAdvicesFlatPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvicesFlatPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvicesFlatPage',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvicesFlatPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advices_flat_page_with_options_async(
        self,
        request: main_models.DescribeAdvicesFlatPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvicesFlatPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvicesFlatPage',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvicesFlatPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advices_flat_page(
        self,
        request: main_models.DescribeAdvicesFlatPageRequest,
    ) -> main_models.DescribeAdvicesFlatPageResponse:
        runtime = RuntimeOptions()
        return self.describe_advices_flat_page_with_options(request, runtime)

    async def describe_advices_flat_page_async(
        self,
        request: main_models.DescribeAdvicesFlatPageRequest,
    ) -> main_models.DescribeAdvicesFlatPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_advices_flat_page_with_options_async(request, runtime)

    def describe_advices_page_with_options(
        self,
        request: main_models.DescribeAdvicesPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvicesPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvicesPage',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvicesPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advices_page_with_options_async(
        self,
        request: main_models.DescribeAdvicesPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvicesPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvicesPage',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvicesPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advices_page(
        self,
        request: main_models.DescribeAdvicesPageRequest,
    ) -> main_models.DescribeAdvicesPageResponse:
        runtime = RuntimeOptions()
        return self.describe_advices_page_with_options(request, runtime)

    async def describe_advices_page_async(
        self,
        request: main_models.DescribeAdvicesPageRequest,
    ) -> main_models.DescribeAdvicesPageResponse:
        runtime = RuntimeOptions()
        return await self.describe_advices_page_with_options_async(request, runtime)

    def describe_advisor_checks_with_options(
        self,
        request: main_models.DescribeAdvisorChecksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvisorChecksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvisorChecks',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvisorChecksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advisor_checks_with_options_async(
        self,
        request: main_models.DescribeAdvisorChecksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvisorChecksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvisorChecks',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvisorChecksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advisor_checks(
        self,
        request: main_models.DescribeAdvisorChecksRequest,
    ) -> main_models.DescribeAdvisorChecksResponse:
        runtime = RuntimeOptions()
        return self.describe_advisor_checks_with_options(request, runtime)

    async def describe_advisor_checks_async(
        self,
        request: main_models.DescribeAdvisorChecksRequest,
    ) -> main_models.DescribeAdvisorChecksResponse:
        runtime = RuntimeOptions()
        return await self.describe_advisor_checks_with_options_async(request, runtime)

    def describe_advisor_checks_fo_pages_with_options(
        self,
        tmp_req: main_models.DescribeAdvisorChecksFoPagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvisorChecksFoPagesResponse:
        tmp_req.validate()
        request = main_models.DescribeAdvisorChecksFoPagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.check_types):
            request.check_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_types, 'CheckTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not DaraCore.is_null(request.biz_category):
            query['BizCategory'] = request.biz_category
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.check_types_shrink):
            query['CheckTypes'] = request.check_types_shrink
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvisorChecksFoPages',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvisorChecksFoPagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advisor_checks_fo_pages_with_options_async(
        self,
        tmp_req: main_models.DescribeAdvisorChecksFoPagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvisorChecksFoPagesResponse:
        tmp_req.validate()
        request = main_models.DescribeAdvisorChecksFoPagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.check_types):
            request.check_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_types, 'CheckTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not DaraCore.is_null(request.biz_category):
            query['BizCategory'] = request.biz_category
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.check_types_shrink):
            query['CheckTypes'] = request.check_types_shrink
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvisorChecksFoPages',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvisorChecksFoPagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advisor_checks_fo_pages(
        self,
        request: main_models.DescribeAdvisorChecksFoPagesRequest,
    ) -> main_models.DescribeAdvisorChecksFoPagesResponse:
        runtime = RuntimeOptions()
        return self.describe_advisor_checks_fo_pages_with_options(request, runtime)

    async def describe_advisor_checks_fo_pages_async(
        self,
        request: main_models.DescribeAdvisorChecksFoPagesRequest,
    ) -> main_models.DescribeAdvisorChecksFoPagesResponse:
        runtime = RuntimeOptions()
        return await self.describe_advisor_checks_fo_pages_with_options_async(request, runtime)

    def describe_advisor_resources_with_options(
        self,
        request: main_models.DescribeAdvisorResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvisorResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvisorResources',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvisorResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advisor_resources_with_options_async(
        self,
        request: main_models.DescribeAdvisorResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvisorResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvisorResources',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvisorResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advisor_resources(
        self,
        request: main_models.DescribeAdvisorResourcesRequest,
    ) -> main_models.DescribeAdvisorResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_advisor_resources_with_options(request, runtime)

    async def describe_advisor_resources_async(
        self,
        request: main_models.DescribeAdvisorResourcesRequest,
    ) -> main_models.DescribeAdvisorResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_advisor_resources_with_options_async(request, runtime)

    def describe_cost_check_advices_with_options(
        self,
        tmp_req: main_models.DescribeCostCheckAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostCheckAdvicesResponse:
        tmp_req.validate()
        request = main_models.DescribeCostCheckAdvicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not DaraCore.is_null(tmp_req.resource_group_id_list):
            request.resource_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_group_id_list, 'ResourceGroupIdList', 'json')
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        if not DaraCore.is_null(tmp_req.tag_list):
            request.tag_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        if not DaraCore.is_null(tmp_req.tag_values):
            request.tag_values_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_values, 'TagValues', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.resource_group_id_list_shrink):
            query['ResourceGroupIdList'] = request.resource_group_id_list_shrink
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        if not DaraCore.is_null(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not DaraCore.is_null(request.tag_values_shrink):
            query['TagValues'] = request.tag_values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostCheckAdvices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostCheckAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cost_check_advices_with_options_async(
        self,
        tmp_req: main_models.DescribeCostCheckAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostCheckAdvicesResponse:
        tmp_req.validate()
        request = main_models.DescribeCostCheckAdvicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not DaraCore.is_null(tmp_req.resource_group_id_list):
            request.resource_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_group_id_list, 'ResourceGroupIdList', 'json')
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        if not DaraCore.is_null(tmp_req.tag_list):
            request.tag_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        if not DaraCore.is_null(tmp_req.tag_values):
            request.tag_values_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_values, 'TagValues', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.resource_group_id_list_shrink):
            query['ResourceGroupIdList'] = request.resource_group_id_list_shrink
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        if not DaraCore.is_null(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not DaraCore.is_null(request.tag_values_shrink):
            query['TagValues'] = request.tag_values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostCheckAdvices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostCheckAdvicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cost_check_advices(
        self,
        request: main_models.DescribeCostCheckAdvicesRequest,
    ) -> main_models.DescribeCostCheckAdvicesResponse:
        runtime = RuntimeOptions()
        return self.describe_cost_check_advices_with_options(request, runtime)

    async def describe_cost_check_advices_async(
        self,
        request: main_models.DescribeCostCheckAdvicesRequest,
    ) -> main_models.DescribeCostCheckAdvicesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cost_check_advices_with_options_async(request, runtime)

    def describe_cost_check_results_with_options(
        self,
        tmp_req: main_models.DescribeCostCheckResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostCheckResultsResponse:
        tmp_req.validate()
        request = main_models.DescribeCostCheckResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not DaraCore.is_null(tmp_req.check_ids):
            request.check_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not DaraCore.is_null(tmp_req.resource_group_id_list):
            request.resource_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_group_id_list, 'ResourceGroupIdList', 'json')
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        if not DaraCore.is_null(tmp_req.tag_list):
            request.tag_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        if not DaraCore.is_null(tmp_req.tag_values):
            request.tag_values_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_values, 'TagValues', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not DaraCore.is_null(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.resource_group_id_list_shrink):
            query['ResourceGroupIdList'] = request.resource_group_id_list_shrink
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        if not DaraCore.is_null(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not DaraCore.is_null(request.tag_values_shrink):
            query['TagValues'] = request.tag_values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostCheckResults',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostCheckResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cost_check_results_with_options_async(
        self,
        tmp_req: main_models.DescribeCostCheckResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostCheckResultsResponse:
        tmp_req.validate()
        request = main_models.DescribeCostCheckResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not DaraCore.is_null(tmp_req.check_ids):
            request.check_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not DaraCore.is_null(tmp_req.resource_group_id_list):
            request.resource_group_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_group_id_list, 'ResourceGroupIdList', 'json')
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        if not DaraCore.is_null(tmp_req.tag_list):
            request.tag_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        if not DaraCore.is_null(tmp_req.tag_values):
            request.tag_values_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_values, 'TagValues', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not DaraCore.is_null(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.resource_group_id_list_shrink):
            query['ResourceGroupIdList'] = request.resource_group_id_list_shrink
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        if not DaraCore.is_null(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not DaraCore.is_null(request.tag_values_shrink):
            query['TagValues'] = request.tag_values_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostCheckResults',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostCheckResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cost_check_results(
        self,
        request: main_models.DescribeCostCheckResultsRequest,
    ) -> main_models.DescribeCostCheckResultsResponse:
        runtime = RuntimeOptions()
        return self.describe_cost_check_results_with_options(request, runtime)

    async def describe_cost_check_results_async(
        self,
        request: main_models.DescribeCostCheckResultsRequest,
    ) -> main_models.DescribeCostCheckResultsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cost_check_results_with_options_async(request, runtime)

    def describe_cost_optimization_overview_with_options(
        self,
        tmp_req: main_models.DescribeCostOptimizationOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostOptimizationOverviewResponse:
        tmp_req.validate()
        request = main_models.DescribeCostOptimizationOverviewShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not DaraCore.is_null(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostOptimizationOverview',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostOptimizationOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cost_optimization_overview_with_options_async(
        self,
        tmp_req: main_models.DescribeCostOptimizationOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostOptimizationOverviewResponse:
        tmp_req.validate()
        request = main_models.DescribeCostOptimizationOverviewShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not DaraCore.is_null(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostOptimizationOverview',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostOptimizationOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cost_optimization_overview(
        self,
        request: main_models.DescribeCostOptimizationOverviewRequest,
    ) -> main_models.DescribeCostOptimizationOverviewResponse:
        runtime = RuntimeOptions()
        return self.describe_cost_optimization_overview_with_options(request, runtime)

    async def describe_cost_optimization_overview_async(
        self,
        request: main_models.DescribeCostOptimizationOverviewRequest,
    ) -> main_models.DescribeCostOptimizationOverviewResponse:
        runtime = RuntimeOptions()
        return await self.describe_cost_optimization_overview_with_options_async(request, runtime)

    def get_history_advices_with_options(
        self,
        request: main_models.GetHistoryAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoryAdvicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoryAdvices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoryAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_history_advices_with_options_async(
        self,
        request: main_models.GetHistoryAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoryAdvicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoryAdvices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoryAdvicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_history_advices(
        self,
        request: main_models.GetHistoryAdvicesRequest,
    ) -> main_models.GetHistoryAdvicesResponse:
        runtime = RuntimeOptions()
        return self.get_history_advices_with_options(request, runtime)

    async def get_history_advices_async(
        self,
        request: main_models.GetHistoryAdvicesRequest,
    ) -> main_models.GetHistoryAdvicesResponse:
        runtime = RuntimeOptions()
        return await self.get_history_advices_with_options_async(request, runtime)

    def get_inspect_progress_with_options(
        self,
        request: main_models.GetInspectProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInspectProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInspectProgress',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInspectProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inspect_progress_with_options_async(
        self,
        request: main_models.GetInspectProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInspectProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInspectProgress',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInspectProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inspect_progress(
        self,
        request: main_models.GetInspectProgressRequest,
    ) -> main_models.GetInspectProgressResponse:
        runtime = RuntimeOptions()
        return self.get_inspect_progress_with_options(request, runtime)

    async def get_inspect_progress_async(
        self,
        request: main_models.GetInspectProgressRequest,
    ) -> main_models.GetInspectProgressResponse:
        runtime = RuntimeOptions()
        return await self.get_inspect_progress_with_options_async(request, runtime)

    def get_product_list_with_options(
        self,
        request: main_models.GetProductListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_list_with_options_async(
        self,
        request: main_models.GetProductListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_list(
        self,
        request: main_models.GetProductListRequest,
    ) -> main_models.GetProductListResponse:
        runtime = RuntimeOptions()
        return self.get_product_list_with_options(request, runtime)

    async def get_product_list_async(
        self,
        request: main_models.GetProductListRequest,
    ) -> main_models.GetProductListResponse:
        runtime = RuntimeOptions()
        return await self.get_product_list_with_options_async(request, runtime)

    def get_task_status_by_id_with_options(
        self,
        request: main_models.GetTaskStatusByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusByIdResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatusById',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_by_id_with_options_async(
        self,
        request: main_models.GetTaskStatusByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusByIdResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatusById',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status_by_id(
        self,
        request: main_models.GetTaskStatusByIdRequest,
    ) -> main_models.GetTaskStatusByIdResponse:
        runtime = RuntimeOptions()
        return self.get_task_status_by_id_with_options(request, runtime)

    async def get_task_status_by_id_async(
        self,
        request: main_models.GetTaskStatusByIdRequest,
    ) -> main_models.GetTaskStatusByIdResponse:
        runtime = RuntimeOptions()
        return await self.get_task_status_by_id_with_options_async(request, runtime)

    def refresh_advisor_check_with_options(
        self,
        tmp_req: main_models.RefreshAdvisorCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAdvisorCheckResponse:
        tmp_req.validate()
        request = main_models.RefreshAdvisorCheckShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_dimension_list):
            request.resource_dimension_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_dimension_list, 'ResourceDimensionList', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        body = {}
        if not DaraCore.is_null(request.resource_dimension_list_shrink):
            body['ResourceDimensionList'] = request.resource_dimension_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAdvisorCheck',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAdvisorCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_advisor_check_with_options_async(
        self,
        tmp_req: main_models.RefreshAdvisorCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAdvisorCheckResponse:
        tmp_req.validate()
        request = main_models.RefreshAdvisorCheckShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_dimension_list):
            request.resource_dimension_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_dimension_list, 'ResourceDimensionList', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not DaraCore.is_null(request.check_id):
            query['CheckId'] = request.check_id
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        body = {}
        if not DaraCore.is_null(request.resource_dimension_list_shrink):
            body['ResourceDimensionList'] = request.resource_dimension_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAdvisorCheck',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAdvisorCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_advisor_check(
        self,
        request: main_models.RefreshAdvisorCheckRequest,
    ) -> main_models.RefreshAdvisorCheckResponse:
        runtime = RuntimeOptions()
        return self.refresh_advisor_check_with_options(request, runtime)

    async def refresh_advisor_check_async(
        self,
        request: main_models.RefreshAdvisorCheckRequest,
    ) -> main_models.RefreshAdvisorCheckResponse:
        runtime = RuntimeOptions()
        return await self.refresh_advisor_check_with_options_async(request, runtime)

    def refresh_advisor_cost_check_with_options(
        self,
        tmp_req: main_models.RefreshAdvisorCostCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAdvisorCostCheckResponse:
        tmp_req.validate()
        request = main_models.RefreshAdvisorCostCheckShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not DaraCore.is_null(tmp_req.check_ids):
            request.check_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not DaraCore.is_null(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.refresh_resource):
            query['RefreshResource'] = request.refresh_resource
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAdvisorCostCheck',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAdvisorCostCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_advisor_cost_check_with_options_async(
        self,
        tmp_req: main_models.RefreshAdvisorCostCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAdvisorCostCheckResponse:
        tmp_req.validate()
        request = main_models.RefreshAdvisorCostCheckShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not DaraCore.is_null(tmp_req.check_ids):
            request.check_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not DaraCore.is_null(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not DaraCore.is_null(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.refresh_resource):
            query['RefreshResource'] = request.refresh_resource
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAdvisorCostCheck',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAdvisorCostCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_advisor_cost_check(
        self,
        request: main_models.RefreshAdvisorCostCheckRequest,
    ) -> main_models.RefreshAdvisorCostCheckResponse:
        runtime = RuntimeOptions()
        return self.refresh_advisor_cost_check_with_options(request, runtime)

    async def refresh_advisor_cost_check_async(
        self,
        request: main_models.RefreshAdvisorCostCheckRequest,
    ) -> main_models.RefreshAdvisorCostCheckResponse:
        runtime = RuntimeOptions()
        return await self.refresh_advisor_cost_check_with_options_async(request, runtime)

    def refresh_advisor_resource_with_options(
        self,
        request: main_models.RefreshAdvisorResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAdvisorResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAdvisorResource',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAdvisorResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_advisor_resource_with_options_async(
        self,
        request: main_models.RefreshAdvisorResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAdvisorResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAdvisorResource',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAdvisorResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_advisor_resource(
        self,
        request: main_models.RefreshAdvisorResourceRequest,
    ) -> main_models.RefreshAdvisorResourceResponse:
        runtime = RuntimeOptions()
        return self.refresh_advisor_resource_with_options(request, runtime)

    async def refresh_advisor_resource_async(
        self,
        request: main_models.RefreshAdvisorResourceRequest,
    ) -> main_models.RefreshAdvisorResourceResponse:
        runtime = RuntimeOptions()
        return await self.refresh_advisor_resource_with_options_async(request, runtime)

    def report_biz_alert_info_with_options(
        self,
        tmp_req: main_models.ReportBizAlertInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportBizAlertInfoResponse:
        tmp_req.validate()
        request = main_models.ReportBizAlertInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alert_uid):
            request.alert_uid_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_uid, 'AlertUid', 'json')
        query = {}
        if not DaraCore.is_null(request.alert_description):
            query['AlertDescription'] = request.alert_description
        if not DaraCore.is_null(request.alert_detail):
            query['AlertDetail'] = request.alert_detail
        if not DaraCore.is_null(request.alert_grade):
            query['AlertGrade'] = request.alert_grade
        if not DaraCore.is_null(request.alert_labels):
            query['AlertLabels'] = request.alert_labels
        if not DaraCore.is_null(request.alert_scene):
            query['AlertScene'] = request.alert_scene
        if not DaraCore.is_null(request.alert_token):
            query['AlertToken'] = request.alert_token
        if not DaraCore.is_null(request.alert_uid_shrink):
            query['AlertUid'] = request.alert_uid_shrink
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReportBizAlertInfo',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportBizAlertInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_biz_alert_info_with_options_async(
        self,
        tmp_req: main_models.ReportBizAlertInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportBizAlertInfoResponse:
        tmp_req.validate()
        request = main_models.ReportBizAlertInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alert_uid):
            request.alert_uid_shrink = Utils.array_to_string_with_specified_style(tmp_req.alert_uid, 'AlertUid', 'json')
        query = {}
        if not DaraCore.is_null(request.alert_description):
            query['AlertDescription'] = request.alert_description
        if not DaraCore.is_null(request.alert_detail):
            query['AlertDetail'] = request.alert_detail
        if not DaraCore.is_null(request.alert_grade):
            query['AlertGrade'] = request.alert_grade
        if not DaraCore.is_null(request.alert_labels):
            query['AlertLabels'] = request.alert_labels
        if not DaraCore.is_null(request.alert_scene):
            query['AlertScene'] = request.alert_scene
        if not DaraCore.is_null(request.alert_token):
            query['AlertToken'] = request.alert_token
        if not DaraCore.is_null(request.alert_uid_shrink):
            query['AlertUid'] = request.alert_uid_shrink
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReportBizAlertInfo',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportBizAlertInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_biz_alert_info(
        self,
        request: main_models.ReportBizAlertInfoRequest,
    ) -> main_models.ReportBizAlertInfoResponse:
        runtime = RuntimeOptions()
        return self.report_biz_alert_info_with_options(request, runtime)

    async def report_biz_alert_info_async(
        self,
        request: main_models.ReportBizAlertInfoRequest,
    ) -> main_models.ReportBizAlertInfoResponse:
        runtime = RuntimeOptions()
        return await self.report_biz_alert_info_with_options_async(request, runtime)
