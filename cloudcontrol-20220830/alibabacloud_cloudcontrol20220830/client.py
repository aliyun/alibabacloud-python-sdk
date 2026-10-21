# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudcontrol20220830 import models as main_models
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
            'ap-northeast-1': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'ap-southeast-6': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'ap-southeast-7': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'cn-beijing': 'cloudcontrol.aliyuncs.com',
            'cn-chengdu': 'cloudcontrol.aliyuncs.com',
            'cn-fuzhou': 'cloudcontrol.aliyuncs.com',
            'cn-guangzhou': 'cloudcontrol.aliyuncs.com',
            'cn-hangzhou': 'cloudcontrol.aliyuncs.com',
            'cn-heyuan': 'cloudcontrol.aliyuncs.com',
            'cn-hongkong': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'cn-huhehaote': 'cloudcontrol.aliyuncs.com',
            'cn-nanjing': 'cloudcontrol.aliyuncs.com',
            'cn-qingdao': 'cloudcontrol.aliyuncs.com',
            'cn-shanghai': 'cloudcontrol.aliyuncs.com',
            'cn-shenzhen': 'cloudcontrol.aliyuncs.com',
            'cn-wulanchabu': 'cloudcontrol.aliyuncs.com',
            'cn-zhangjiakou': 'cloudcontrol.aliyuncs.com',
            'us-west-1': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'me-central-1': 'cloudcontrol.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'cloudcontrol.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudcontrol', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tasks/{DaraURL.percent_encode(task_id)}/operation/cancel',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tasks/{DaraURL.percent_encode(task_id)}/operation/cancel',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        task_id: str,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(task_id, headers, runtime)

    async def cancel_task_async(
        self,
        task_id: str,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(task_id, headers, runtime)

    def create_resource_with_options(
        self,
        request_path: str,
        request: main_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request_path: str,
        request: main_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request_path: str,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(request_path, request, headers, runtime)

    async def create_resource_async(
        self,
        request_path: str,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_with_options_async(request_path, request, headers, runtime)

    def delete_resource_with_options(
        self,
        request_path: str,
        tmp_req: main_models.DeleteResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        tmp_req.validate()
        request = main_models.DeleteResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        request_path: str,
        tmp_req: main_models.DeleteResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        tmp_req.validate()
        request = main_models.DeleteResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        request_path: str,
        request: main_models.DeleteResourceRequest,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(request_path, request, headers, runtime)

    async def delete_resource_async(
        self,
        request_path: str,
        request: main_models.DeleteResourceRequest,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_with_options_async(request_path, request, headers, runtime)

    def get_api_price_with_options(
        self,
        request: main_models.GetApiPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiPriceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GetApiPrice',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/price/quote',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_price_with_options_async(
        self,
        request: main_models.GetApiPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiPriceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GetApiPrice',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/price/quote',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_price(
        self,
        request: main_models.GetApiPriceRequest,
    ) -> main_models.GetApiPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_api_price_with_options(request, headers, runtime)

    async def get_api_price_async(
        self,
        request: main_models.GetApiPriceRequest,
    ) -> main_models.GetApiPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_api_price_with_options_async(request, headers, runtime)

    def get_price_with_options(
        self,
        request_path: str,
        tmp_req: main_models.GetPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPriceResponse:
        tmp_req.validate()
        request = main_models.GetPriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_attributes):
            request.resource_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_attributes, 'resourceAttributes', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_attributes_shrink):
            query['resourceAttributes'] = request.resource_attributes_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrice',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_price_with_options_async(
        self,
        request_path: str,
        tmp_req: main_models.GetPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPriceResponse:
        tmp_req.validate()
        request = main_models.GetPriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_attributes):
            request.resource_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_attributes, 'resourceAttributes', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_attributes_shrink):
            query['resourceAttributes'] = request.resource_attributes_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrice',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_price(
        self,
        request_path: str,
        request: main_models.GetPriceRequest,
    ) -> main_models.GetPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_price_with_options(request_path, request, headers, runtime)

    async def get_price_async(
        self,
        request_path: str,
        request: main_models.GetPriceRequest,
    ) -> main_models.GetPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_price_with_options_async(request_path, request, headers, runtime)

    def get_resource_type_with_options(
        self,
        request_path: str,
        headers: main_models.GetResourceTypeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypeResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = str(headers.x_acs_accept_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetResourceType',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        request_path: str,
        headers: main_models.GetResourceTypeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypeResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = str(headers.x_acs_accept_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetResourceType',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type(
        self,
        request_path: str,
    ) -> main_models.GetResourceTypeResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetResourceTypeHeaders()
        return self.get_resource_type_with_options(request_path, headers, runtime)

    async def get_resource_type_async(
        self,
        request_path: str,
    ) -> main_models.GetResourceTypeResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetResourceTypeHeaders()
        return await self.get_resource_type_with_options_async(request_path, headers, runtime)

    def get_resources_with_options(
        self,
        request_path: str,
        tmp_req: main_models.GetResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourcesResponse:
        tmp_req.validate()
        request = main_models.GetResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResources',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resources_with_options_async(
        self,
        request_path: str,
        tmp_req: main_models.GetResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourcesResponse:
        tmp_req.validate()
        request = main_models.GetResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResources',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resources(
        self,
        request_path: str,
        request: main_models.GetResourcesRequest,
    ) -> main_models.GetResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resources_with_options(request_path, request, headers, runtime)

    async def get_resources_async(
        self,
        request_path: str,
        request: main_models.GetResourcesRequest,
    ) -> main_models.GetResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resources_with_options_async(request_path, request, headers, runtime)

    def get_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        task_id: str,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    async def get_task_async(
        self,
        task_id: str,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(task_id, headers, runtime)

    def get_terraform_pricing_mappings_with_options(
        self,
        request: main_models.GetTerraformPricingMappingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTerraformPricingMappingsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GetTerraformPricingMappings',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/price/terraform-mappings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTerraformPricingMappingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_terraform_pricing_mappings_with_options_async(
        self,
        request: main_models.GetTerraformPricingMappingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTerraformPricingMappingsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GetTerraformPricingMappings',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/price/terraform-mappings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTerraformPricingMappingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_terraform_pricing_mappings(
        self,
        request: main_models.GetTerraformPricingMappingsRequest,
    ) -> main_models.GetTerraformPricingMappingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_terraform_pricing_mappings_with_options(request, headers, runtime)

    async def get_terraform_pricing_mappings_async(
        self,
        request: main_models.GetTerraformPricingMappingsRequest,
    ) -> main_models.GetTerraformPricingMappingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_terraform_pricing_mappings_with_options_async(request, headers, runtime)

    def list_data_sources_with_options(
        self,
        request_path: str,
        tmp_req: main_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        tmp_req.validate()
        request = main_models.ListDataSourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.attribute_name):
            query['attributeName'] = request.attribute_name
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        request_path: str,
        tmp_req: main_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        tmp_req.validate()
        request = main_models.ListDataSourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.attribute_name):
            query['attributeName'] = request.attribute_name
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        request_path: str,
        request: main_models.ListDataSourcesRequest,
    ) -> main_models.ListDataSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(request_path, request, headers, runtime)

    async def list_data_sources_async(
        self,
        request_path: str,
        request: main_models.ListDataSourcesRequest,
    ) -> main_models.ListDataSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_sources_with_options_async(request_path, request, headers, runtime)

    def list_products_with_options(
        self,
        provider: str,
        request: main_models.ListProductsRequest,
        headers: main_models.ListProductsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = str(headers.x_acs_accept_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/providers/{DaraURL.percent_encode(provider)}/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        provider: str,
        request: main_models.ListProductsRequest,
        headers: main_models.ListProductsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = str(headers.x_acs_accept_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/providers/{DaraURL.percent_encode(provider)}/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        provider: str,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListProductsHeaders()
        return self.list_products_with_options(provider, request, headers, runtime)

    async def list_products_async(
        self,
        provider: str,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListProductsHeaders()
        return await self.list_products_with_options_async(provider, request, headers, runtime)

    def list_resource_types_with_options(
        self,
        provider: str,
        product: str,
        tmp_req: main_models.ListResourceTypesRequest,
        headers: main_models.ListResourceTypesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypesResponse:
        tmp_req.validate()
        request = main_models.ListResourceTypesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_types):
            request.resource_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types, 'resourceTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_types_shrink):
            query['resourceTypes'] = request.resource_types_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = str(headers.x_acs_accept_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypes',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/providers/{DaraURL.percent_encode(provider)}/products/{DaraURL.percent_encode(product)}/resourceTypes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        provider: str,
        product: str,
        tmp_req: main_models.ListResourceTypesRequest,
        headers: main_models.ListResourceTypesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypesResponse:
        tmp_req.validate()
        request = main_models.ListResourceTypesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_types):
            request.resource_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_types, 'resourceTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_types_shrink):
            query['resourceTypes'] = request.resource_types_shrink
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = str(headers.x_acs_accept_language)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypes',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/providers/{DaraURL.percent_encode(provider)}/products/{DaraURL.percent_encode(product)}/resourceTypes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(
        self,
        provider: str,
        product: str,
        request: main_models.ListResourceTypesRequest,
    ) -> main_models.ListResourceTypesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListResourceTypesHeaders()
        return self.list_resource_types_with_options(provider, product, request, headers, runtime)

    async def list_resource_types_async(
        self,
        provider: str,
        product: str,
        request: main_models.ListResourceTypesRequest,
    ) -> main_models.ListResourceTypesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListResourceTypesHeaders()
        return await self.list_resource_types_with_options_async(provider, product, request, headers, runtime)

    def list_supported_pricing_apis_with_options(
        self,
        request: main_models.ListSupportedPricingApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportedPricingApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportedPricingApis',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/price/supported-apis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportedPricingApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_supported_pricing_apis_with_options_async(
        self,
        request: main_models.ListSupportedPricingApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportedPricingApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportedPricingApis',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/price/supported-apis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportedPricingApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_supported_pricing_apis(
        self,
        request: main_models.ListSupportedPricingApisRequest,
    ) -> main_models.ListSupportedPricingApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_supported_pricing_apis_with_options(request, headers, runtime)

    async def list_supported_pricing_apis_async(
        self,
        request: main_models.ListSupportedPricingApisRequest,
    ) -> main_models.ListSupportedPricingApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_supported_pricing_apis_with_options_async(request, headers, runtime)

    def update_resource_with_options(
        self,
        request_path: str,
        request: main_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        request_path: str,
        request: main_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2022-08-30',
            protocol = 'HTTPS',
            pathname = f'{request_path}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        request_path: str,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(request_path, request, headers, runtime)

    async def update_resource_async(
        self,
        request_path: str,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_with_options_async(request_path, request, headers, runtime)
